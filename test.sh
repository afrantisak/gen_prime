#!/usr/bin/env bash

python prime.py 100000  | diff test_data/prime.1e5.out -
#python prime.py 1000000 | diff test_data/prime.1e6.out -
python prime_deltas.py 400 | diff test_data/prime_deltas.400.out -
