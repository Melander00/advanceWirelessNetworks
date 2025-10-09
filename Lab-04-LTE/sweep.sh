#!/usr/bin/env bash

# Setup 
cd /work 
source scripts/setup_env.sh
cd "$NS3_DIR"

# Part 1
for dataRate in 5Mbps 10Mbps 20Mbps 30Mbps 50Mbps 75Mbps 100Mbps; do
    echo ""
    echo "--- Rate" $dataRate "Seed" 1 "----"
    ns3 run --quiet exec -- --dataRate=$dataRate --csv=/work/Lab-04-LTE/submission/throughput_datarate.csv
    cp DlPdcpStats.txt /work/Lab-04-LTE/submission/trace_1_$dataRate.txt
    cp DlRlcStats.txt /work/Lab-04-LTE/submission/trace_1_rlc_$dataRate.txt
    # ns3 run --quiet exec -- --antenna=cosine --dataRate=$dataRate --seed=1 --csv=/work/Lab-04-LTE/submission/p1.csv
    # ns3 run --quiet exec -- --antenna=parabolic --dataRate=$dataRate --seed=1 --csv=/work/Lab-04-LTE/submission/p1.csv
done

# Part 2
# for distance in 5000 10000 15000 20000; do
#     echo ""
#     echo "--- Distance" $distance "----"
#     ns3 run --quiet exec -- --distance=$distance --dataRate=10Mbps --csv=/work/Lab-04-LTE/submission/p2.csv
#     cp DlPdcpStats.txt /work/Lab-04-LTE/submission/trace_2_$distance.txt
# done