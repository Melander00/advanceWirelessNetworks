````markdown
# Lab 01 – Wireless Propagation Models

This lab explores how different propagation loss models in ns-3 affect wireless communication range and throughput. You will simulate throughput vs. distance under various models, and then compare simulation results with real-world path-loss measurements.


## Learning Goals
- Learn how to configure different propagation models in ns-3 (Friis, Two-Ray Ground, COST231-Hata).
- Understand how distance impacts throughput for each model.
- Compare simulation-based path loss with measured path loss.
- Practice generating CSV results and plotting graphs.


## Provided Files
- **docs/**
  - `Lab-01-Instructions.md` – step-by-step instructions.
  - `deliverables.md` – required submission files.
- **code/**
  - `Lab1_Cpp_Friis.cc`, `Lab1_Cpp_TwoRay.cc`, `Lab1_Cpp_Cost231.cc`
  - `Lab1_Py_Friis.py`, `Lab1_Py_TwoRay.py`, `Lab1_Py_Cost231.py`

Each file sets up a two-node Wi-Fi link and applies the respective propagation model.

````
## Running the Code

### C++ path
1. Copy the desired `.cc` file into your ns-3 `scratch/` directory.
2. Build and run, e.g.:
   ```bash
   cd ~/ns-allinone-3.40/ns-3.40
   ./ns3 build
   ./ns3 run scratch/Lab1_Cpp_Friis


3. Capture output data into a CSV as required (you may need to redirect or modify code to log distance vs throughput).

### Python path

1. Ensure `PYTHONPATH` is set (or use Docker).
2. Run, e.g.:

   ```bash
   python3 Lab-01-Propagation/code/Lab1_Py_Friis.py
   ```
3. Save results into the specified CSV files.

---

## Data Collection

* Vary the **distance** between nodes (as instructed in the PDF).
* For each model, record throughput at multiple distances.
* Save results to:

  * `friis_results.csv`, `two_ray_results.csv`, `cost231_results.csv`
* Generate corresponding plots:

  * `friis_plot.png`, `two_ray_plot.png`, `cost231_plot.png`

Additionally, collect **real-world measurements** (RSSI vs distance), compute path loss, and compare with Friis model:

* `measured_pathloss.csv`
* `friis_pathloss.csv`
* `pathloss_comparison.png`

---

## Deliverables Checklist

(see `docs/deliverables.md` for details)

* `choice.txt` – either `C++` or `Python`
* Simulation CSVs and plots for each model
* Measured vs Friis CSVs and comparison plot

---

## Common Pitfalls

* **Wrong Wi-Fi rate string:** Use `"DsssRate5_5Mbps"` (underscore, not dot) to avoid *“no matching DataMode”* errors.
* **Insufficient distance points:** Use enough distance values to clearly show the drop in throughput.
* **Path loss calculation:** Ensure you convert RSSI to path loss correctly (in dB).
* **Plot labeling:** Every plot must have axes labels and a legend.

---
