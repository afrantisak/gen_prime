import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sets
import math
import lib.prime
import lib.plot

def get_deltas(iterable, init):
    x = []
    y = []
    last = init
    for num in iterable:
        x += [num]
        y += [num - last]
        last = num
    return x, y

def get_prime_deltas(maximum):
    return get_deltas(lib.prime.generate_less_than(maximum), 1)

def plot_prime_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    lib.plot.show_2d(x, y)

def plot_prime_dbl_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    deltas = sets.Set(y)
    lib.plot.rainbow_range(deltas)
    xy = zip(x, y)
    x2 = []
    y2 = []
    z2 = []
    for index, n in enumerate(deltas):
        xyf = [p for p in xy if p[1] == n]
        if not xyf: continue
        xf, yf = zip(*xyf)
        xn, yn = get_deltas(xf, 0)
        x2 += [n] * len(xn)
        y2 += [math.log(y) for y in yn]
        z2 += [colors[index]] * len(xn)
    lib.plot.show_2d(x2, y2, z2)

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    #plot_prime_dbl_deltas(num)
    plot_prime_deltas(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
