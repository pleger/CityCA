#For every experiment, the previous experiment is removed

#!/bin/sh
rm log.txt
./cleanExpResults.sh > log.txt
nohup python Benchmarks.py $1 >> log.txt &


