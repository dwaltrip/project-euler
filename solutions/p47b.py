from itertools import chain, izip_longest, count
from math import sqrt
from collections import defaultdict
import sys
import timeit

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
        
class PrimeFactorCache(object):
    def __init__(self):
        self.prime_generator = gen_primes()
        self.primes = {}
        self.factors = {}
                    
    def update_cache(self, maxnum):
        for p in chain(self.primes, self.prime_generator):
            if p:
                if p not in self.primes:
                    self.primes[p] = p
                while True:
                    multiple = self.primes[p]
                    if multiple in self.factors:
                        self.factors[multiple] += 1
                    else:
                        self.factors[multiple] = 1
                    self.primes[p] += p
                    if maxnum < multiple + p:
                        break
            else:
                break
                
def main():
    SEQ_LENGTH = 4
    pfc = PrimeFactorCache()
    limit = 1000000
    pfc.update_cache(limit)
    factor_list = sorted(pfc.factors.iteritems())
    in_a_row = 0
    for n, factor_count in factor_list:
        if factor_count == SEQ_LENGTH:
            in_a_row += 1
        else:
            in_a_row = 0
        if in_a_row == SEQ_LENGTH:
            return n - SEQ_LENGTH + 1
        
def main2():
    SEQ_LENGTH = 4
    LIMIT = 1000000
    factors = {}
    for p in gen_primes():
        if p > LIMIT:
            break
        for m in count(1):
            multiple = m*p
            if multiple in factors:
                factors[multiple] += 1
            else:
                factors[multiple] = 1
            if multiple > LIMIT - p:
                break
    in_a_row = 0
    for n, factor_count in sorted(factors.iteritems()):
        if factor_count == SEQ_LENGTH:
            in_a_row += 1
        else:
            in_a_row = 0
        if in_a_row == SEQ_LENGTH:
            return n - SEQ_LENGTH + 1
            
def prime_factor_count(n, cache):
    if not n in cache:
        cache[n] = 1
        for d in xrange(2, int(sqrt(n))+1):
            if n%d==0:
                cache[n] = cache[n/d] + 1 if (n/d)%d != 0 else cache[n/d]
                break
    return cache[n]

def main3():
    cache = {}
    in_a_row = 0
    for i in count(2):
        if prime_factor_count(i, cache) == 4:
            in_a_row += 1
        else:
            in_a_row = 0
        if in_a_row == 4:
            return i-2
            
def main4():
    sieve = {} # {(x = multiple of prime p) >= i: [p, known factor count in x]}
    for i in count(2):          # count from 2 upwards
        if i not in sieve:      # if i is prime:
            want = 4            #   want 4 consecutive integers
            p = i
        else:
            p, factors = sieve.pop(i)  # have now noted all factors of i
            if factors < 4:     # non-prime i has less than 4 prime factors
                want = 4
            else:
                want -= 1
                if want == 0:
                    return i-3
        # p divides i; find next unoccupied multiple of p in sieve
        while 1:
            i += p
            if i not in sieve: break
            sieve[i][1] += 1    # found one more factor (p) of i
        sieve[i] = [p, 1]       # so far, i has 1 known factor (p)
        
def main5():
    lim = 1000000
    seq_length = 4
    sieve = [0] * lim
    goal = [seq_length] * seq_length
    for i in xrange(2,int(sqrt(lim)) + 1):
        if sieve[i] == 0:
            sieve[i+i::i] = [x + 1 for x in sieve[i+i::i]]
    for i in xrange(2,len(sieve) - seq_length):
        if sieve[i:i+seq_length] == goal:
            return i
            
if __name__ == '__main__':
    print main2()
    t = timeit.Timer('main2()', 'from __main__ import main2').timeit(1)
    print 'Time:', t