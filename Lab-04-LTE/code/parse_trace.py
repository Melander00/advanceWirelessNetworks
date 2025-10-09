import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser(description='Parse trace file and calculate total bytes and throughput.')
parser.add_argument('filename', type=str, help='Name of the trace .txt file inside submission folder.')
parser.add_argument('--csv', type=bool, help="Sets print format as csv file instead.", default=False)
parser.add_argument('--total', type=bool, help="Whether each row should be combined to a total.", default=False)
parser.add_argument('--bytesField', type=str, help="The field that should get the bytes from TxBytes or RxBytes.", default="TxBytes")

args = parser.parse_args()

# Paths
repo = Path("../")
file_path  = repo / "submission" / args.filename
outd = repo / "submission"
outd.mkdir(parents=True, exist_ok=True)








# Read header manually
with open(file_path, 'r') as f:
    header_line = f.readline().strip()
    if header_line.startswith('%'):
        header_line = header_line[1:]  # Remove leading '%'
    columns = [c.strip() for c in header_line.split('\t')]  # strip spaces

# If first column is empty, remove it
if columns[0] == '' or columns[0] == ' ':
    columns = columns[1:]

# Fix repeated columns (stdDev, min, max)
fixed_columns = []
parent = None
for col in columns:
    if col in ['stdDev', 'min', 'max']:
        fixed_columns.append(f"{parent}_{col}")
    else:
        fixed_columns.append(col)
        parent = col

# Read the rest of the file
df = pd.read_csv(file_path, sep='\t', skiprows=1, names=fixed_columns, index_col=False)

# Strip any spaces from column names to be extra safe
df.columns = [c.strip() for c in df.columns]

# Debug: print columns to verify
# print("Columns detected:", df.columns.tolist())

df['start'] = df['start'].astype(float)
df['end'] = df['end'].astype(float)


# print(df[['start', 'end']].head())
# print(df.dtypes)


# Ensure numeric columns
df = df.apply(pd.to_numeric, errors='coerce')

# Calculate total bytes delivered (TxBytes + RxBytes)
df['TotalBytes'] = df['TxBytes'] + df['RxBytes']
df['TotalBytesDelivered'] = df[args.bytesField]

# Calculate duration for each row
df['Duration'] = df['end'] - df['start']

# Calculate throughput in bits per second
df['Throughput_bps'] = df['TotalBytes'] * 8 / df['Duration']

# Print results

if args.total == True:
    total_tx_bytes = df[args.bytesField].sum()
    total_duration = df['end'].iloc[-1] - df['start'].iloc[0]
    overall_throughput_bps = total_tx_bytes * 8 / total_duration
    print(f"Total Tx = {total_tx_bytes}, Total Duration = {total_duration}, Total Throughput = {overall_throughput_bps}")
else:
    if args.csv == True:
        print("tx_bytes,duration,throughput")
        for idx, row in df.iterrows():
            print(f"{row['TotalBytesDelivered']},{row['Duration']},{row['Throughput_bps']}")
    else: 
        for idx, row in df.iterrows():
            print(f"Row {idx}: Total Bytes Delivered (Tx) = {row['TotalBytesDelivered']}, Duration = {row['Duration']}, Throughput (bps) = {row['Throughput_bps']}")