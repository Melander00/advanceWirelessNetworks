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

# Ensure numeric types (important!)
df['num_nodes'] = pd.to_numeric(df['num_nodes'])
df['pkt_size'] = pd.to_numeric(df['pkt_size'])
df['throughput'] = pd.to_numeric(df['throughput'])

# Average throughput over seeds
avg_df = df.groupby(['num_nodes', 'pkt_size'], as_index=False)['throughput'].mean()

# Sort for correct line plotting
avg_df = avg_df.sort_values(by=['pkt_size', 'num_nodes'])

# Plot
plt.figure(figsize=(8, 5))
for pkt_size, group in avg_df.groupby('pkt_size'):
    plt.plot(group['num_nodes'], group['throughput'] / (10**6), marker='o', label=f'pkt_size={pkt_size}')

plt.xlabel('Number of Nodes')
plt.ylabel('Average Throughput (Mbps)')
plt.title('Throughput vs Number of Nodes (Averaged over Seeds)')
plt.legend(title='Packet Size')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

outfile = outd / "sweep.png"
plt.savefig(outfile, dpi=300)

plt.show()