import sys
import lib.prime

def print_primes_less_than(num):
    last = 1
    for prime in lib.prime.generate_less_than(num):
        print prime#, prime - last
        last = prime

def print_prime_deltas_less_than(num):
    last = 1
    cur_max = 0
    for prime in lib.prime.generate_less_than(num):
        delta = prime - last
        if cur_max < delta:
           cur_max = delta
           print
        print "%5d  %5d" % (prime, delta)
        last = prime
    
def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print_primes_less_than(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
