from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "sweep.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Convert rate_mbps to numeric (strip "Mbps")
df["rate_float"] = df["rate_mbps"].str.replace("Mbps", "", regex=False).astype(float)

# Average throughput across seeds
df_avg = df.groupby(["rate_float", "payload"], as_index=False)["throughput"].mean()

# Convert throughput to Mbps
df_avg["throughput_mbps"] = df_avg["throughput"] / 1e6

# Plot
plt.figure(figsize=(7,5))

for payload, group in df_avg.groupby("payload"):
    plt.plot(group["rate_float"], group["throughput_mbps"],
             marker="o", label=f"Payload {payload} B")

plt.xlabel("PHY Rate (Mbps)")
plt.ylabel("Throughput (Mbps)")
plt.title("Throughput vs PHY Rate for Different Payload Sizes")
plt.legend()
plt.grid(True)
plt.tight_layout()

outfile = outd / "sweep.png"
plt.savefig(outfile, dpi=300)
plt.show()