import sys
import matplotlib.pyplot as plt
import numpy as np
import prime

def plot_primes_less_than(maximum):
    x = [1]
    y = [0]
    last = 1
    for num in prime.generate_less_than(maximum):
        x += [num]
        y += [num - last]
        last = num
        
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    plt.show()

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    plot_primes_less_than(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
