#!/bin/sh
rm log.txt
./cleanExpResults.sh > log.txt
nohup python Benchmarks.py >> log.txt &

