#!/usr/bin/env bash

# Setup 
cd /work 
source scripts/setup_env.sh
cd "$NS3_DIR"

# # # Adhoc
# for pktSize in 1200; do
#     for numNodes in 3 4 5 6; do
#         for seed in 1 2; do
#             ns3 run --quiet exec -- --pktSize=$pktSize --seed=$seed --numNodes=$numNodes --distance=51
#         done
#     done
# done

# # Sweep
# for pktSize in 300 700 1200; do
#     for numNodes in 3 4 5 6; do
#         for seed in 1 2; do
#             ns3 run --quiet exec -- --pktSize=$pktSize --seed=$seed --numNodes=$numNodes --distance=50
#         done
#     done
# done

# TCP
for tcp in 0 1; do
    for pktSize in 300 1200; do
        for seed in 1 2; do
            ns3 run --quiet exec -- --tcp=$tcp --pktSize=$pktSize --seed=$seed --distance=50
        done
    done
done


# # Hidden
# for rts in 0 1; do
#     for seed in 1; do
#         ns3 run --quiet exec -- --enableRtsCts=$rts --seed=$seed --pktSize=1000 --distance=55
#     done
# done