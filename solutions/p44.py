from itertools import count
from math import sqrt
import timeit

def gen_pentagonal():
    for i in count(1):
        yield (i*(3*i - 1))/2

def isPentagonal(n):
    x = (1 + sqrt(1 + 24*n))/6.0
    if x == int(x):
        return True
    return False
    
### second implementation,  (first one was ungodly slow at ~6 minutes), but doesn't guarantee 100% answer is the smallest
def main():
    pentagonals = []
    lookup = set()
    n = 0
    for new_p in gen_pentagonal():
        for i in xrange(n-1,-1,-1):
            p = pentagonals[i]
            if new_p - p in lookup and abs(p - (new_p - p)) in lookup:
                print 'sum:', new_p, '-- p1:', p, '-- p2:', new_p - p, '-- difference:', abs(p - (new_p - p))
                return abs(p - (new_p - p))            
        pentagonals.append(new_p)
        lookup.add(new_p)
        n += 1        

# guarantees that 'diff' will be the smallest, as we use each
def main2():
    pentagonals = []
    lookup = set()
    n = 0
    for diff in gen_pentagonal():
        for i in xrange(n-1,-1,-1):
            p1 = pentagonals[i]
            p2 = p1 + diff
            if isPentagonal(p2) and isPentagonal(p1 + p2):
                print 'p1:', p1, '-- p2:', p2, '-- sum:', p1 + p2, '-- diff:', diff
                return diff
        pentagonals.append(diff)
        lookup.add(diff)
        n += 1

if __name__ == '__main__':
    print main2()
    t = timeit.Timer('main2()','from __main__ import main2').timeit(1)
    print 'Time:', t