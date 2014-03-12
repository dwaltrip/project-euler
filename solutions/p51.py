import math
from itertools import combinations
import timeit

def prime_check(maxnum):
	"""Returns a function that checks if a number < maxnum is prime"""
	bucket = range(int(math.sqrt(maxnum)) + 1)
	bucket[1] = 0
	for i in bucket:
		if i <> 0:
			for not_prime in xrange(2*i, int(math.sqrt(maxnum)) +1, i):
				bucket[not_prime] = 0
	bucket = filter(lambda x: x <> 0, bucket)
	
	def isPrime(num):
		for i in bucket:
			if num % i == 0:
				return False
			if i > math.sqrt(num):
				return True
		return True
	
	return isPrime

def replacements(s, places):
	start = 1 if 0 in places else 0
	for r in map(str, xrange(start, 10)):
		yield ''.join(r if pos in places else c for pos, c in enumerate(s))            
			
def main():
	MAX = 10**6
	isPrime = prime_check(MAX)
	tested_already = set()
	zz = []
	i = 1001
	while i<MAX:
		s = str(i)
		if s not in tested_already:
			for places in combinations(range(len(s)-1),3):
				c = 0
				for p in replacements(s, places):
					if isPrime(int(p)):
						c += 1
					tested_already.add(p)
				if c == 8:
					return i, places
		i += 2
	print len(tested_already)
	print 'tested up to: %s' % MAX
	print xx
	
def main2():
	MAX = 2*10**5
	isPrime = prime_check(MAX)
	tested_already = set()
	
	
	
if __name__ == '__main__':
	print main()
	t = timeit.Timer('main()','from __main__ import main').timeit(1)
	print 'Time:',t