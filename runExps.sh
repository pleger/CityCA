#!/bin/sh
rm log.txt

# To work with mail, it is necessary to config sendmail
nohup python Benchmarks.py > log.txt &

