# Lab 4 Deliverables

## Part 1 – Trace Collection

1. **Simulation trace files**

   * `DlRlcStats.trace` — raw RLC layer trace from `LteHelper`.
   * `DlPdcpStats.trace` — raw PDCP layer trace from `LteHelper`.

2. **PCAP evidence**

   * `server_trace.pcap` — packet capture recorded on the server’s side.

---

## Part 2 – Antenna Configurations

1. **Results summary**

   * `antenna_config_comparison.txt` — short description of differences observed in traces for parabolic, cosine, and isotropic antennas.
   * Mention cases where UE is not aligned with directional antennas.

---

## Part 3 – Throughput vs. Data Rate

1. **Simulation results**

   * `throughput_vs_rate.csv` — columns:

     ```
     data_rate_mbps,throughput_bps
     ```

     with at least 3 different application data rates.

2. **Plot**

   * `throughput_vs_rate_plot.png` — plot showing DL throughput vs. application data rate.

---

## Part 4 – Throughput vs. Distance

1. **Simulation results**

   * `throughput_vs_distance.csv` — columns:

     ```
     distance_m,throughput_bps
     ```

     using isotropic antenna and varying UE distance.

2. **Plot**

   * `throughput_vs_distance_plot.png` — plot showing DL throughput vs. distance.

---

## Part 5 – Discussion

1. **Analysis files**

   * `trace_choice.txt` — explain whether `DlRlcStats` or `DlPdcpStats` was used for throughput calculation, and why.
   * `conclusions.txt` — discussion of observed throughput trends and differences across antenna configurations and distances.

---

## File Naming Summary

* `DlRlcStats.trace`, `DlPdcpStats.trace`, `server_trace.pcap`
* `antenna_config_comparison.txt`
* `throughput_vs_rate.csv`, `throughput_vs_rate_plot.png`
* `throughput_vs_distance.csv`, `throughput_vs_distance_plot.png`
* `trace_choice.txt`, `conclusions.txt`

---

**All CSVs must include headers. All plots must include labeled axes and legends. File names must match exactly.**
