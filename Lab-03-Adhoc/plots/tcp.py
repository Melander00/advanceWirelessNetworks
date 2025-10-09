from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Paths
repo = Path("../")
csv  = repo / "submission" / "tcp.csv"
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)

# Load CSV file
df = pd.read_csv(csv)

# Ensure numeric columns
df['pkt_size'] = pd.to_numeric(df['pkt_size'])
df['throughput'] = pd.to_numeric(df['throughput'])

# Average throughput across seeds for each (protocol, pkt_size)
avg_df = df.groupby(['protocol', 'pkt_size'], as_index=False)['throughput'].mean()

# Sort for correct line plotting
avg_df = avg_df.sort_values(by=['protocol', 'pkt_size'])

# Plot
plt.figure(figsize=(8, 5))
for protocol, group in avg_df.groupby('protocol'):
    plt.plot(group['pkt_size'], group['throughput'] / (10**6), marker='o', label=protocol)

# Labels and styling
plt.xlabel('Packet Size')
plt.ylabel('Average Throughput')
plt.title('Throughput vs Packet Size (Averaged over Seeds)')
plt.legend(title='Protocol')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

outfile = outd / "tcp.png"
plt.savefig(outfile, dpi=300)

# Display the plot
plt.show()