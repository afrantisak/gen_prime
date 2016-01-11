import sys
import math
import itertools

def get_deltas(iterable, init):
    x = []
    y = []
    last = init
    for num in iterable:
        x += [num]
        y += [num - last]
        last = num
    return x, y

def ideltas(iterable, init_value):
    last = init_value
    for num in iterable:
        yield num, num - last
        last = num
x
