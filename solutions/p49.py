from itertools import permutations, combinations
from collections import defaultdict
from math import sqrt
import timeit

def prime_check(maxnum):
	"""Returns a function that checks if a number < maxnum is prime"""
	bucket = range(int(sqrt(maxnum)) + 1)
	bucket[1] = 0
	for i in bucket:
		if i <> 0:
			for not_prime in xrange(2*i, int(sqrt(maxnum)) +1, i):
				bucket[not_prime] = 0
	bucket = filter(lambda x: x <> 0, bucket)
	
	def isPrime(num):
		for i in bucket:
			if num % i == 0:
				return False
			if i > sqrt(num):
				return True
		return True
	
	return isPrime

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

def main():
    is_prime = prime_check(10000)
    prime_pooper = gen_primes()
    for p in prime_pooper:
        if p == 997:
            break
    checked = set()
    sols = set()
    for prime in prime_pooper:
        if prime not in checked:
            perms = [int(''.join(s)) for s in set(permutations(str(prime)))]
            perms = [x for x in perms if (x>999 and is_prime(x))]
            for x1,x2,x3 in combinations(perms, 3):
                x1,x2,x3 = sorted((x1,x2,x3))
                if x3 - x2 == x2 - x1:
                    sols.add((x1,x2,x3))
            for p in perms:
                checked.add(p)
        if prime > 9999:
            break
    return sols
                    
if __name__ == "__main__":
    print main()
    t = timeit.Timer('main()','from __main__ import main').timeit(1)
    print 'Time:', t