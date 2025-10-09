#!/usr/bin/env bash

# Setup 
cd /work 
source scripts/setup_env.sh
cd "$NS3_DIR"

# Part 1
for dataRate in 5Mbps 10Mbps 20Mbps; do
    # for seed in 1 2; do
        echo ""
        echo "--- Rate" $dataRate "Seed" 1 "----"
        ns3 run --quiet exec -- --dataRate=$dataRate
        cp DlPdcpStats.txt /work/Lab-04-LTE/submission/trace_1_$dataRate.txt
        # ns3 run --quiet exec -- --antenna=cosine --dataRate=$dataRate --seed=1 --csv=/work/Lab-04-LTE/submission/p1.csv
        # ns3 run --quiet exec -- --antenna=parabolic --dataRate=$dataRate --seed=1 --csv=/work/Lab-04-LTE/submission/p1.csv
    # done
done