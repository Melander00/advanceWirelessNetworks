from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "scenario1.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Clean up rate_mbps column: remove "Mbps" and convert to float
df["rate_mbps"] = df["rate_mbps"].str.replace("Mbps", "", regex=False).astype(float)

# Convert throughput columns from bps → Mbps
for col in ["seed1_bps", "seed2_bps", "avg_bps"]:
    df[col] = df[col] / 1e6

# Group by PHY rate (in case multiple runs exist per rate)
grouped = df.groupby("rate_mbps").agg(
    mean_seed1=("seed1_bps", "mean"),
    std_seed1=("seed1_bps", "std"),
    mean_seed2=("seed2_bps", "mean"),
    std_seed2=("seed2_bps", "std"),
    mean_avg=("avg_bps", "mean"),
    std_avg=("avg_bps", "std"),
).reset_index()

# Replace NaNs in std with 0 (avoids StopIteration when only one sample per rate)
grouped = grouped.fillna(0)

# Plot
plt.figure(figsize=(10, 6))

plt.errorbar(grouped["rate_mbps"], grouped["mean_seed1"], yerr=grouped["std_seed1"],
             fmt="o-", capsize=5, label="Seed 1")
plt.errorbar(grouped["rate_mbps"], grouped["mean_seed2"], yerr=grouped["std_seed2"],
             fmt="s-", capsize=5, label="Seed 2")
plt.errorbar(grouped["rate_mbps"], grouped["mean_avg"], yerr=grouped["std_avg"],
             fmt="^-", capsize=5, label="Average")

# Labels and title
plt.xlabel("PHY Rate (Mbps)")
plt.ylabel("Application Throughput (Mbps)")
plt.title("Mean Application Throughput vs. PHY Rate")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save figure
outfile = outd / "scenario1.png"
plt.tight_layout()
plt.savefig(outfile, dpi=300)
plt.show()
