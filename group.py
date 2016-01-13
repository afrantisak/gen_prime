import sys
import lib.plot
import lib.prime
import lib.vector

def get_prime_deltas(maximum):
    primes = list(lib.prime.generate_less_than(maximum))
    deltas = list(lib.vector.deltas(primes, 1))
    return primes, deltas

def group_by(primes, deltas):
    pd = zip(primes, deltas)
    cur_max = 0
    group = []
    for prime, delta in pd:
        if cur_max < delta:
           cur_max = delta
           if group:
               yield group
               group = []
        group.append((prime, delta))
    yield group        

def plot(maximum):
    delta_groups = []
    for group in group_by(*get_prime_deltas(maximum)):
        primes, deltas = zip(*group)
        delta_groups.append(deltas)
    group_xs = []
    group_ys = []
    group_zs = []
    colors = lib.plot.rainbow_range(delta_groups)
    for group_index, group in enumerate(delta_groups):
        group_spacing = 100.0 / (len(group) - 1)
        group_max = max(group)
        group_normalized = [100.0 * delta / group_max for delta in group]
        y = group_normalized
        x = []
        for n in range(len(group)):
            xn = n * group_spacing
            x.append(xn)
        group_xs += x
        group_ys += y
        group_zs += [colors[group_index]] * len(group)
        #print "gs", group_spacing
        #print "x", x
        #print "y", y
    lib.plot.show_2d(group_xs, group_ys, group_zs)
    #print "x", group_xs
    #print "y", group_ys
    #print 

def main():
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    plot(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
