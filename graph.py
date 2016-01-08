import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import prime
import sets

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
    return get_deltas(prime.generate_less_than(maximum), 1)

def plot_prime_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    plot_2d(x, y)

def plot_prime_dbl_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    deltas = sets.Set(y)
    colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(deltas)))
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
        y2 += yn
        z2 += [colors[index]] * len(xn)
    plot_2d(x2, y2, z2)

def plot_2d(x, y, c=None):
    max_x = max(x)
    max_y = max(y)
    edg_x = max_x * 0.05
    edg_y = max_y * 0.05
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, c=c)
    ax.axis([-edg_x, max_x + edg_x, -edg_y, max_y + edg_y])
    plt.show()

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    plot_prime_dbl_deltas(num)
    #plot_prime_deltas(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
