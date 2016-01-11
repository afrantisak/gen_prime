import sys
import math
import itertools

def ideltas(iterable, init_value):
    last = init_value
    for num in iterable:
        yield num - last
        last = num

