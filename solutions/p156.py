from math import log10
from itertools import izip

class DigitTracker(object):
    def __init__(self):
        self.powers_complete = 2
        self.cache = {1:{0:1, 1:1}, 2:{0:10,1:20}}
        self.solutions = {}
        for i in xrange(10):
            self.solutions[i] = []

    def build_cache(self, max_p):
        for p in xrange(self.powers_complete + 1, max_p + 1):
            digit_dict = {0:(10**(p-2)-1)*10, 1:10**(p-1)}
            for d in digit_dict:
                digit_dict[d] += self.cache[p-1][d]*10
            self.cache[p] = digit_dict
        self.powers_complete = max_p
        
    def f(self, n, d):
        P = int(log10(n))
        if P + 1 > self.powers_complete:
            self.build_cache(P+1)
        num_str = str(n)
        k = 1 if d else 0
        s = 0
        extra_zeros = sum(10**p for p in xrange(P, 0, -1))
        for dig_str,p in izip(num_str,xrange(P,0,-1)):
            dig = int(dig_str)
            if d:
                s += self.cache[p][k] * dig
                if dig > d:
                    s += 10**p
                elif dig == d:
                    s += (n % (10**p)) + 1
            else:
                s += self.cache[p][k]*dig + (extra_zeros-1)/10 * (dig-1)
                if p < P and extra_zeros:
                    s += extra_zeros
                extra_zeros = (extra_zeros-1)/10 
        if int(num_str[-1]) >= d:
            s += 1
        return s
        
    def search_matches(self, d):
        p = 1
        while True:
        
def bisearcher(dt, a, b, d):
    fa,fb = dt.f(a,d), dt.f(b,d)
    while True:
        mid = (a + b)/2
        fm = dt.f(mid, d)
        if fm == mid:
            return mid
        elif fm > mid:
            b = mid
        else:
            a = mid
        c += 1
        if c > 200:
            print 'a:',a,'-- b:',b,'-- mid:',mid,'-- fm:', fm
            return
                
def find_sol(dt, d):
	p = 1
	c = 0
	while True:
		x = (d+1)*(10**p)-1
		fx = dt.f(x,d)
		if fx > x:
			return bisearcher(dt, (x+1)/10 - 1, x, d)
		p += 1
		c += 1
		if c > 500:
			print 'x:',x,'-- fx:', fx, '-- p:', p
			return
            