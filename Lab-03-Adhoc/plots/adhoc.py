from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "adhoc.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Group by num_nodes and pkt_size, then average throughput across seeds
avg_df = df.groupby(['num_nodes', 'pkt_size'], as_index=False)['throughput'].mean()

# Plot
plt.figure(figsize=(8, 5))
for pkt_size, group in avg_df.groupby('pkt_size'):
    plt.plot(group['num_nodes'], group['throughput'] / (10**6), marker='o', label=f'pkt_size={pkt_size}')

# Labels and styling
plt.xlabel('Number of Nodes')
plt.ylabel('Average Throughput (Mbps)')
plt.title('Throughput vs Number of Nodes (Averaged over Seeds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 
outfile = outd / "adhoc.png"
plt.savefig(outfile, dpi=300)

# Show the plot
plt.show()