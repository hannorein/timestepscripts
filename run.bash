#!/bin/bash
#
for i in $(seq 0 39);
do
    ./rebound $1 $i
done
wait
