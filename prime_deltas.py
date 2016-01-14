import sys
import lib.prime

def printable(num):
    if num is not None:
        if isinstance(num, int):
            return "%5d %s" % (num, even_odd(num))
        else:
            return "%7s" % num
    else:
        return '     '

def delta(a, b):
    if b is not None:
        return a - b
    return None
        
def even_odd(num):
    if num is None:
        return " "
    return "o" if num % 2 else "e"

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

def print_prime_deltas_less_than(num, depth):
    print printable("index"), printable('prime'),
    for d in range(depth - 1):
        print printable("d%d" % d),
    print printable("d%d/2" % d)
    for index, deltas in enumerate(get_deltas(lib.prime.generate_less_than(num), depth)):
        if even_odd(index) != 'e':
            continue
        print printable(index),
        for d in range(depth):
            print printable(deltas[d]),
        if deltas[depth - 1] is not None:
            print printable(deltas[depth - 1] / 2),
        print

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    deltas = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    print_prime_deltas_less_than(num, deltas)
    return 0

if __name__ == "__main__":
    sys.exit(main())
