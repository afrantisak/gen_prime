import sys
import lib.prime

def print_primes_less_than(num):
    for prime in lib.prime.generate_less_than(num):
        print prime

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print_primes_less_than(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
