from math import log10
from itertools import count
import cProfile 
import timeit

def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    if n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = n**.5
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True

def L2R(n):
    power = int(log10(n))
    for p in xrange(power,0,-1):
        yield n%(10**p)

def R2L(n):
    power = int(log10(n)+1)
    for p in xrange(1,power):
        yield (n - n%(10**p))/(10**p)

def main():
    counter = 0
    truncatable_primes = []
    power = 2
    for k in count(4):
        for i in [k*6-1, k*6+1]:
            s = str(i)
            if '0' not in s and '4' not in s and '6' not in s and '8' not in s and '1' != s[0] and '1' != s[len(s)-1] and isPrime(i):
                truncatable = True
                for n1 in R2L(i):
                    if not isPrime(n1):
                        truncatable = False
                        break
                if truncatable:
                    for n2 in L2R(i):
                        if not isPrime(n2):
                            truncatable = False
                            break
                    if truncatable:
                        truncatable_primes.append(i)
                        counter += 1
                        if counter == 11:
                            return truncatable_primes
                    else:
                        continue
                else:
                    continue
            else:
                continue
                
def check_truncs(n):
    for i in R2L(n):
        if not isPrime(i):
            return False
    for i in L2R(n):
        if not isPrime(i):
            return False
    return True

class PrimeFinder(object):
    def __init__(self):
        self.primes = set()
        self.not_primes = set([1])
    def isPrime(self,n):
        if n in self.primes:
            return True
        elif n in self.not_primes:
            return False
        else:
            if n == 2:
                self.primes.add(n)
                return True
            if n%2 == 0:
                self.not_primes.add(n)
                return False
            if n < 9: 
                self.primes.add(n)
                return True
            if n%3 == 0:
                self.not_primes.add(n)
                return False
            r = n**.5
            f = 5
            while f <= r:
                if n%f == 0:
                    self.not_primes.add(n)
                    return False
                if n%(f+2) == 0:
                    self.not_primes.add(n)
                    return False
                f += 6
            self.primes.add(n)
            return True

def main2():
    # pf = PrimeFinder()
    def check_prime_simple(num):
        if num == 1:
            return False
        for i in xrange(2, num):
            if i**2 > num :
                return True
            if num % i == 0:
                break
                return False
 
    def check_subprimes(prime):
        prime_str = str(prime)
        for i in xrange(1, len(prime_str)):
            substr = prime_str[i:]
            # if not check_prime_simple(int(substr)):
            if not isPrime(int(substr)):
                return False
        return True
     
    primes = []
    def build_prime(prime):
        global total
        for i in (1, 3, 7, 9):
            new_prime = prime * 10 + i
            # if check_prime_simple(new_prime):
            if isPrime(new_prime):
                if check_subprimes(new_prime):
                # if check_truncs(new_prime):
                    primes.append(new_prime)
                build_prime(new_prime)
     
    build_prime(2)
    build_prime(3)
    build_prime(5)
    build_prime(7)
    return primes    
    
if __name__ == '__main__':
    tp = main()
    print tp
    print sum(tp)
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:', t.timeit(1)
    cProfile.run('main()')