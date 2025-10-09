from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "throughput_distance.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Convert distance from meters to kilometers
df['distance_km'] = df['distance_m'] / 1000

# Plot
plt.figure(figsize=(8,5))
plt.plot(df['distance_km'], df['throughput_bps'] / (10**6), marker='o', label='UE Throughput')
plt.plot(df['distance_km'], df['dl_throughput'] / (10**6), marker='o', label='DL Throughput')

# Labels and styling
plt.xlabel('Distance (km)')
plt.ylabel('Throughput (Mbps)')
plt.title('Throughput vs Distance')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

outfile = outd / "throughput_vs_distance.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")

plt.show()