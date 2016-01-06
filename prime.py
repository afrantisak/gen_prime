import math

def generator():
    yield 2
    num = 3
    while True:
        if all(num % i != 0 for i in xrange(2, int(math.sqrt(num)) + 1)):
            yield num
        num += 2

def primes_less_than(max):
    gen = generator()
    num = gen.next()
    while num < max:
        print num
        num = gen.next()
    
def main():
    return primes_less_than(100000)

if __name__ == "__main__":
    main()
