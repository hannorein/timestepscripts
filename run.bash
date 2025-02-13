#!/bin/bash
#
for i in $(seq 0 79);
do
    ./rebound $1 $i &
done
wait
