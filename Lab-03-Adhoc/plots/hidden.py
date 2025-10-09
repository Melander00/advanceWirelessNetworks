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


# Calculate total throughput
df['throughput_total'] = df['throughput_f0'] + df['throughput_f1']

# Ensure correct order (OFF, ON)
df['rts'] = pd.Categorical(df['rts'], categories=['OFF', 'ON'], ordered=True)
df = df.sort_values('rts')

# Plot
plt.figure(figsize=(8, 5))

plt.plot(df['rts'], df['throughput_f0'], marker='o', label='Flow 0')
plt.plot(df['rts'], df['throughput_f1'], marker='o', label='Flow 1')
plt.plot(df['rts'], df['throughput_total'], marker='o', linestyle='--', label='Total')

# Labels and styling
plt.xlabel('RTS Setting')
plt.ylabel('Throughput')
plt.title('Throughput vs RTS Setting (per Flow and Total)')
plt.legend(title='Flow')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

outfile = outd / "hidden.png"
plt.savefig(outfile, dpi=300)

# Show the plot
plt.show()