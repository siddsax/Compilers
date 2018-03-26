#!/bin/bash
python3 main.py $1 > $1.s
gcc -m32 $1.s
./a.out
