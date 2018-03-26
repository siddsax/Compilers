#!/bin/bash
python3 main.py ../test/example$1.ir > ../test/example$1.s
gcc -m32 ../test/example$1.s
./a.out