import sys
import lib.prime

def print_primes_less_than(num):
    last = 1
    for prime in lib.prime.generate_less_than(num):
        print prime#, prime - last
        last = prime

def printable(num):
    if num is not None:
        return "%5d" % num
    else:
        return '     '

def delta(a, b):
    if b is not None:
        return a - b
    return None
        
def get_deltas(iterable, depth):
    import collections, copy
    deltas = [None] * depth
    last = copy.copy(deltas)
    for num in iterable:
        deltas[0] = num
        for d in range(1, depth):
            deltas[d] = delta(deltas[d-1], last[d-1])
        yield deltas
        last = copy.copy(deltas)

def print_prime_deltas_less_than(num, depth=3):
    for deltas in get_deltas(lib.prime.generate_less_than(num), depth):
        for d in range(depth):
            print printable(deltas[d]),
        print

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    deltas = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    if deltas:
        print_prime_deltas_less_than(num, deltas)
    else:
        print_primes_less_than(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
