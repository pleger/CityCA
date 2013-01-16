#!/bin/sh
rm log.txt

nohup python Benchmarks.py > log.txt &

