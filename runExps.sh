#!/bin/sh
nohup python Benchmarks.py > log.txt &
# To work with mail, it is necessary to config sendmail
echo "Available results :D" | mail -s "ChileCA Available" pleger@gmail.com
