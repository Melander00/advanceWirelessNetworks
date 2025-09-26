from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "twotriangles.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Convert rate_mbps like "1Mbps" → 1.0 (float)
df["rate_mbps"] = df["rate_mbps"].str.replace("Mbps", "", regex=False).astype(float)

# Ensure numeric values for throughput columns
for col in ["flow1", "flow2", "aggr"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Group by rate_mbps, average across seeds
avg_df = df.groupby("rate_mbps", as_index=False)[["flow1", "flow2", "aggr"]].mean()

# Convert throughput from bps → Mbps
avg_df[["flow1", "flow2", "aggr"]] /= 1e6

# Plot
plt.figure(figsize=(8,6))
plt.plot(avg_df["rate_mbps"], avg_df["flow1"], marker="o", label="Flow1 Avg")
plt.plot(avg_df["rate_mbps"], avg_df["flow2"], marker="s", label="Flow2 Avg")
plt.plot(avg_df["rate_mbps"], avg_df["aggr"], marker="^", linewidth=2.5, color="black", label="Aggregate Avg")

plt.title("Scenario 1 Two Triangles: Average Throughput vs PHY Rate")
plt.xlabel("PHY Rate (Mbps)")
plt.ylabel("Throughput (Mbps)")
plt.xticks(avg_df["rate_mbps"])  # ensure ticks at 1.0, 5.5, 11.0
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

# Save and show
outfile = outd / "twotriangles.png"
plt.savefig(outfile, dpi=300)
plt.show()
