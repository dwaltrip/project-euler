from collections import defaultdict
from itertools import count
import sys
import timeit

class PrimeList(object):
    def __init__(self):
        self.primes = []
        self.generator = gen_primes()
        
    def __iter__(self):
        for p in self.primes:
            yield p
        for p in self.generator:
            self.primes.append(p)
            yield p

def gen_primes():
    """ Generate an infinite sequence of prime numbers."""
    D = defaultdict(list)
    q = 2
    while True:
        if q not in D:

            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D[p + q].append(p)
            del D[q]
        q += 1
   
def num_prime_factors(n, primes):
    s = 0
    for p in primes:
        if n%p==0:
            s += 1
        while n%p==0:
            n /= p
        if n == 1:
            break
    return s
        
def check(n, primes):
    in_a_row = 0
    for i in xrange(n-3,n+4,1):
        if num_prime_factors(i, primes) == 4:
            in_a_row += 1
            if in_a_row == 4:
                return i-3, i-2, i-1, i
        else:
            in_a_row = 0
    return False
        
def main():
    in_a_row = 0
    primes = PrimeList()
    for i in xrange(1, sys.maxint, 4):
        if num_prime_factors(i, primes) == 4:
            sol = check(i, primes)
            if sol:
                return sol
        if i > 134045:
            return 'You suck!'

if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t
        