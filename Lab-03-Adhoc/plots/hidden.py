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
df['pdr_avg'] = (df['pdr_f0'] + df['pdr_f1']) / 2

# Ensure correct order (OFF, ON)
df['rts'] = pd.Categorical(df['rts'], categories=['OFF', 'ON'], ordered=True)
df = df.sort_values('rts')

# Plot
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(df['rts'], df['throughput_f0'], marker='o', label='Flow 0')
ax.plot(df['rts'], df['throughput_f1'], marker='o', label='Flow 1')
ax.plot(df['rts'], df['throughput_total'], marker='o', linestyle='--', label='Total')

# Labels and styling
ax.set_xlabel('RTS Setting')
ax.set_ylabel('Throughput')
ax.set_title('Throughput vs RTS Setting (per Flow and Total)')
ax.legend(title='Flow')
ax.grid(True, linestyle='--', alpha=0.6)

outfile = outd / "hidden.png"
fig.savefig(outfile, dpi=300)

# PDR Plot
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(df['rts'], df['pdr_f0'], marker='o', label='Flow 0')
ax.plot(df['rts'], df['pdr_f1'], marker='o', label='Flow 1')
ax.plot(df['rts'], df['pdr_avg'], marker='o', linestyle='--', label='Average')

ax.set_xlabel('RTS Setting')
ax.set_ylabel('PDR')
ax.set_title('PDR vs RTS Setting (per Flow and Average)')
ax.legend(title='Flow')
ax.grid(True, linestyle='--', alpha=0.6)

outfile = outd / "hidden_pdr.png"
fig.savefig(outfile, dpi=300)

# Show the plot
plt.show()