import sys
import lib.vector
import lib.plot

def get_prime_deltas(maximum):
    primes = list(lib.prime.generate_less_than(maximum))
    deltas = list(lib.vector.deltas(primes, 1))
    return primes, deltas

def plot_prime_deltas(maximum):
    x, y = get_prime_deltas(maximum)
    lib.plot.show_2d(x, y)

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    plot_prime_deltas(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
