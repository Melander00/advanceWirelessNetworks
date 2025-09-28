from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "hidden.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Strip 'Mbps' and convert to float
df["rate_float"] = df["rate_mbps"].str.replace("Mbps", "", regex=False).astype(float)

# Average over seeds
df_avg = df.groupby(["rate_float", "rts"], as_index=False)[["flow1", "flow2", "aggr"]].mean()

# --- First two plots: one per RTS ---
for rts_val, group in df_avg.groupby("rts"):
    fig, ax = plt.subplots(figsize=(7,5))
    ax.plot(group["rate_float"], group["flow1"]/1e6, marker="o", label="Flow 1")
    ax.plot(group["rate_float"], group["flow2"]/1e6, marker="s", label="Flow 2")
    ax.plot(group["rate_float"], group["aggr"]/1e6, marker="^", label="Aggregate")
    
    ax.set_xlabel("PHY Rate (Mbps)")
    ax.set_ylabel("Throughput (Mbps)")
    ax.set_title(f"Throughput vs PHY Rate (RTS = {rts_val})")
    ax.grid(True)
    ax.legend()
    
    outfile = outd / f"hidden_rts{rts_val}.png"
    fig.savefig(outfile, dpi=300, bbox_inches="tight")

# --- Comparison plot: Aggregate ---
fig, ax = plt.subplots(figsize=(7,5))
for rts_val, group in df_avg.groupby("rts"):
    ax.plot(group["rate_float"], group["aggr"]/1e6, marker="o", label=f"RTS={rts_val}")
ax.set_xlabel("PHY Rate (Mbps)")
ax.set_ylabel("Aggregate Throughput (Mbps)")
ax.set_title("Aggregate Throughput vs PHY Rate (RTS Comparison)")
ax.grid(True)
ax.legend()
outfile = outd / "hidden_comparison.png"
fig.savefig(outfile, dpi=300, bbox_inches="tight")

# --- Comparison plot: Flow1 ---
fig, ax = plt.subplots(figsize=(7,5))
for rts_val, group in df_avg.groupby("rts"):
    ax.plot(group["rate_float"], group["flow1"]/1e6, marker="o", label=f"RTS={rts_val}")
ax.set_xlabel("PHY Rate (Mbps)")
ax.set_ylabel("Flow 1 Throughput (Mbps)")
ax.set_title("Flow 1 Throughput vs PHY Rate (RTS Comparison)")
ax.grid(True)
ax.legend()
outfile = outd / "hidden_flow1_comparison.png"
fig.savefig(outfile, dpi=300, bbox_inches="tight")

# --- Comparison plot: Flow2 ---
fig, ax = plt.subplots(figsize=(7,5))
for rts_val, group in df_avg.groupby("rts"):
    ax.plot(group["rate_float"], group["flow2"]/1e6, marker="o", label=f"RTS={rts_val}")
ax.set_xlabel("PHY Rate (Mbps)")
ax.set_ylabel("Flow 2 Throughput (Mbps)")
ax.set_title("Flow 2 Throughput vs PHY Rate (RTS Comparison)")
ax.grid(True)
ax.legend()
outfile = outd / "hidden_flow2_comparison.png"
fig.savefig(outfile, dpi=300, bbox_inches="tight")

plt.show()