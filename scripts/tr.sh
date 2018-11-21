#!/bin/bash

f1 = "0.1 0.3 0.5"
f2 = "9 8 7"
f3 = "3 89 12"

for d in $f1 $f2 $f3; do
	for t in $d; do
		echo $t
	done
done
