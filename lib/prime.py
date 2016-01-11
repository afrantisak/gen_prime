import math
import itertools

def is_a(num):
    return all(num % i != 0 for i in xrange(3, int(math.sqrt(num)) + 1))

def is_not_divisible(num, den):
    return num % den != 0

def is_b(num):
    return all(is_not_divisible(num, i) for i in xrange(3, int(math.sqrt(num)) + 1))

def generate():
    yield 2
    num = 3
    while True:
        if is_a(num):
            yield num
        num += 2

def generate_less_than(maximum):
    return itertools.takewhile(lambda num: num < maximum, generate())

