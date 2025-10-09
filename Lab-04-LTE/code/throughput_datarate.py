from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "throughput_datarate.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Convert data_rate from string (e.g., "10Mbps") to numeric value in Mbps
df['data_rate_Mbps'] = df['data_rate'].str.replace('Mbps','').astype(float)

# Plot
plt.figure(figsize=(8,5))
plt.plot(df['data_rate_Mbps'], df['throughput_bps'] / (10**6), marker='o', label='UE Throughput')
plt.plot(df['data_rate_Mbps'], df['dl_throughput'] / (10**6), marker='o', label='DL Throughput')

# Labels and styling
plt.xlabel('Datarate (Mbps)')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput vs Datarate')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

outfile = outd / "throughput_datarate.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")

plt.show()