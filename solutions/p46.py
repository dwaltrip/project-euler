from math import sqrt
import sys
from itertools import ifilterfalse, dropwhile, count
import timeit
import cProfile

def isPrime(n):
    if n==2 or n==3: return True
    elif n==1 or n%2==0 or n%3==0: return False
    elif n < 24: return True
    r = int(sqrt(n))
    k = 5
    while k <= r:
        if n%k==0 or n%(k+2)==0: return False
        k += 6
    return True
    
def gen_square_terms(n):
    upper_bound = int(sqrt(n/2))
    for i in xrange(1,upper_bound+1):
        yield 2 * i**2
        
def main():
    for n in xrange(9, sys.maxint, 2):
        if not isPrime(n):
            for k in gen_square_terms(n):
                if isPrime(n-k):
                    break
            else:
                return n
                
def fits_pattern(odd_composite):
   for double_square in (2*n*n for n in count(1)):
      prime = odd_composite - double_square
      if prime < 2:
        break # consider '1' as a prime too
      elif isPrime(prime):
         return True     
   return False
   
##the following is a very nifty use of generators and the itertools module
def main2():
    odd_composites = ifilterfalse(isPrime, xrange(9, 10**9, 2))
    return dropwhile(fits_pattern, odd_composites).next()
            
if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t
    cProfile.run('main()')