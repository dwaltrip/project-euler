from math import sqrt
import timeit

def gen_perms(chars):
	if len(chars)<=1:
		yield chars
	else:
		for p in gen_perms(chars[1:]):
			for i in xrange(len(p)+1):
				yield p[:i] + chars[0] + p[i:]

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
    
def isPandigital(k):
    num = sorted(str(k))
    for i in xrange(len(num)):
        if str(i+1) != num[i]:
            return False
    return True

def main():
    ## it has to be 7 digits long because any pandigital 8-digit number or 9-digit number is divisible by 3
    s = '1234567'
    pandigitals = sorted([int(s) for s in gen_perms(s)], reverse=True)
    for p in pandigitals:
        if isPrime(p):
            return p
            
if __name__ == '__main__':
    sol = main()
    print 'solution:', sol
    t = timeit.Timer('main()', 'from __main__ import main')
    t1 = t.timeit(1)
    print 'Time:', t1