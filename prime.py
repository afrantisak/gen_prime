import sys
import math
import itertools

def is_prime(num):
    return all(num % i != 0 for i in xrange(2, int(math.sqrt(num)) + 1))

def generate():
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2

def generate_less_than(max):
    return itertools.takewhile(lambda num: num < max, generate())

def print_primes_less_than(max):
    for prime in generate_less_than(max):
        print prime
    
def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print_primes_less_than(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
