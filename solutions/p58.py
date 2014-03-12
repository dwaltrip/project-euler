from math import sqrt
from itertools import count
import timeit

def isPrime(n):
    if n==1: return False
    elif n==2 or n==3: return True
    elif n==1 or n%2==0 or n%3==0: return False
    elif n < 24: return True
    r = int(sqrt(n))
    k = 5
    while k <= r:
        if n%k==0 or n%(k+2)==0: return False
        k += 6
    return True
    
def main():
    tr,dtr = 3,2
    tl,dtl = 5,4
    bl,dbl = 7,6
    num_primes = 3
    total = 5
    N = 3
    done = False
    while not done:
        dtr += 8
        dtl += 8
        dbl += 8
        tr += dtr
        tl += dtl
        bl += dbl
        #print 'tr:', tr, '~ tl:', tl, '~ bl:', bl
        num_primes += 1 if isPrime(tr) else 0
        num_primes += 1 if isPrime(tl) else 0
        num_primes += 1 if isPrime(bl) else 0
        total += 4
        N += 2
        if ((num_primes * 1.0) / total) < .1:
            print N
            done = True

if __name__ == "__main__":
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t