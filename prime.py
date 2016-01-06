import math

def generator():
    yield 2
    for num in xrange(3,100001,2):
        if all(num % i != 0 for i in xrange(2, int(math.sqrt(num)) + 1)):
            yield num

for num in generator():
    print num            
