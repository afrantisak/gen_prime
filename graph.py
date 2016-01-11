import sys
import sets
import math
import lib.prime
import lib.plot
import lib.vector

def get_prime_deltas(maximum):
    primes = list(lib.prime.generate_less_than(maximum))
    deltas = list(lib.vector.ideltas(primes, 1))
    return primes, deltas

def plot_prime_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    lib.plot.show_2d(x, y)

def plot_prime_dbl_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    unique_deltas = sets.Set(y)
    lib.plot.rainbow_range(unique_deltas)
    xy = zip(x, y)
    x2 = []
    y2 = []
    z2 = []
    for index, n in enumerate(unique_deltas):
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
