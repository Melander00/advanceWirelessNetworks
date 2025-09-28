#!/usr/bin/env bash

# Setup 
cd /work 
source scripts/setup_env.sh
cd "$NS3_DIR"

# Part 1

# for rate in 1 5.5 11; do
#     for seed in 1 2; do
#         ns3 run --quiet exec -- --rate=$rate --seed=$seed
#     done
# done



# Sweep
# # Rate loop
# for rate in 1 5.5 11; do
#     # Payload loop
#     for payload in 400 700 1000; do
#         # Seed loop
#         for seed in 1 2; do
#             # Run ns3
#             ns3 run --quiet exec -- -rate=$rate --payload=$payload --seed=$seed --distance=25
#         done
#     done
# done



# Hidden
for rate in 1 5.5 11; do
    for rts in 0 2200; do
        for seed in 1 2; do
            ns3 run --quiet exec -- --rate=$rate --seed=$seed --rts=$rts --distance=5
        done
    done
done