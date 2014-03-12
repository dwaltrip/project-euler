from itertools import count
from timeit import Timer

def main():
    for i in count(2):
        lower = 10**i
        upper = int(round(10**i + (10**i)*(2.0/3)))
        for n in xrange(lower, upper):
            good = True
            basis = set(str(n))
            for k in xrange(2,7):
                if basis != set(str(n*k)):
                    good = False
                    break
            if good:
                return n

if __name__ == '__main__':
    print main()
    t = Timer('main()', 'from __main__ import main')
    print 'Time:', t.timeit(1)
