
# Simulation Background

This document provides an overview of the simulation architecture used by [ns-3](https://www.nsnam.org/), the discrete-event network simulator employed in the labs. Understanding these core principles will help you write correct simulations, generate reproducible results, and debug effectively.

---

## 1. What is Discrete-Event Simulation (DES)?

Unlike real-time simulators or emulators, ns-3 uses a **discrete-event simulation (DES)** model. In DES:

- Time advances **in discrete steps** based on the timestamps of scheduled events.
- Each event corresponds to a function call (callback) that modifies the simulation state.
- Events are processed **sequentially**, in strict timestamp order.
- If multiple events are scheduled for the same time, they are resolved using a deterministic secondary ordering (event ID).

There is **no real-world time constraint**: the simulation might take seconds or minutes to run depending on the complexity, but the simulation time behaves as though it’s unfolding continuously.

> 🔎 More: [NS-3 Manual – Events](https://www.nsnam.org/docs/manual/html/events.html)

---

## 2. NS-3 Simulation Core: How Events Work

The simulator maintains an **event queue**, which stores scheduled events with the form:

```

\[ simulation\_time, function\_to\_execute ]

````

You schedule events using:

```cpp
Simulator::Schedule(Seconds(10.0), &MyFunction);
````

This will run `MyFunction` at simulation time `t = 10.0s`. The actual wall-clock time at which this happens is irrelevant to the simulation.

NS-3’s event loop continues until:

* The event queue is empty, or
* You explicitly stop it using `Simulator::Stop()`.

To run the simulation, you invoke:

```cpp
Simulator::Run();
Simulator::Destroy(); // Clean up
```

Key methods:

* `Simulator::Now()` returns current simulation time.
* `Simulator::Schedule()`, `ScheduleNow()`, and `ScheduleWithContext()` allow flexible scheduling.

More: [Simulator API docs](https://www.nsnam.org/doxygen/classns3_1_1_simulator.html)

---

## 3. Randomness and Reproducibility

### Why Seeds Matter

NS-3 uses **random number generators (RNGs)** in mobility models, error models, traffic generators, etc. Without fixed seeds, your results may differ from run to run — making debugging and reproducibility nearly impossible.

You must set:

```cpp
RngSeedManager::SetSeed(12345);   // Set global seed
RngSeedManager::SetRun(7);        // Vary run number for multiple experiments
```

* The **seed** fixes the random number sequence space.
* The **run number** picks a different stream within that space.
* This lets you repeat experiments exactly (same seed and run) or get statistically distinct runs (same seed, different run).

> 🔎 More: [RngSeedManager API](https://www.nsnam.org/doxygen/classns3_1_1_rng_seed_manager.html)

### Good Practice

* Always set both seed and run explicitly at the start of every experiment.
* When analyzing performance, **run the same scenario multiple times** with different run numbers to obtain averages and error bars.

---

## 4. Best Practices in Simulation Design

**Determinism**: Ensure your simulation is deterministic when intended. Avoid hidden nondeterminism (e.g., object creation order in scripts).

**Repeatability**: Fix seeds and run numbers. Use `--RngRun` as a command-line argument to easily vary the run in batch scripts.

**Statistical Validity**: Do not rely on a single run. Run at least 3–5 independent simulations and report the mean and standard deviation.

**Time Granularity**: NS-3 supports high-resolution time (`Time::SetResolution(Time::NS);`) — but setting overly small time steps may increase computational cost without benefit.

**Logging**: Use `NS_LOG` macros for debugging. Example:

```cpp
NS_LOG_INFO("At time " << Simulator::Now().GetSeconds() << "s, sending packet.");
```

Enable logs with:

```sh
NS_LOG="UdpClient=level_info|prefix_time" ./waf --run scratch/my-sim
```

More: [NS-3 Logging Guide](https://www.nsnam.org/docs/tutorial/html/getting-started.html#using-the-ns-3-logging-environment)

---

## 5. Example: Putting It All Together

```cpp
#include "ns3/core-module.h"

using namespace ns3;

void MyCallback() {
    std::cout << "At " << Simulator::Now().GetSeconds() << "s, Event executed!" << std::endl;
}

int main() {
    RngSeedManager::SetSeed(12345);
    RngSeedManager::SetRun(1);

    Simulator::Schedule(Seconds(2.0), &MyCallback);
    Simulator::Schedule(Seconds(5.0), &MyCallback);

    Simulator::Run();
    Simulator::Destroy();
}
```

Output:

```
At 2s, Event executed!
At 5s, Event executed!
```

This confirms that simulation time progresses by event execution, not wall time.

---

## 6. Resources

* [NS-3 Manual: Events and Simulation Time](https://www.nsnam.org/docs/manual/html/events.html)
* [Simulator Class Documentation](https://www.nsnam.org/doxygen/classns3_1_1_simulator.html)
* [RNG Best Practices (ns-3 wiki)](https://www.nsnam.org/wiki/Random_Variables)
* [NS-3 Logging Overview](https://www.nsnam.org/docs/tutorial/html/getting-started.html#using-the-ns-3-logging-environment)

---