from math import sqrt
import timeit

def product_combos(n,values):
	if n == 1:
		return values
	lst = []
	for i,v in enumerate(values):
		t = product_combos(n-1,values[i+1:])
		for c in t:
			lst.append(v*c)
	return lst
    
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
    
    ## this WILL NOT WORK.. primes is length 42, and 42choose21 = 538257874440, which is way too many divisors
def p266():
    primes = [i for i in xrange(2,190) if isPrime(i)]
    print len(primes)
    divisors = []
    for i in xrange(1, len(primes)+1):
        print i,
        if i != len(primes):
            print '~',
        divisors.extend(product_combos(i,primes))
    print len(divisors)
    divisors.sort()
    p = 1
    for prime in primes:
        p *= primes
    for i,d in enumerate(divisors):
        if d**2 > p:
            print divisors[i-1]
            break

if __name__ == '__main__':
    s1,s2 = 'p266()','from __main__ import p266'
    t = timeit.Timer(s1,s2).timeit(1)
    print 'Time:',t