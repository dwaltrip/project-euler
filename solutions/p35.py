import math
import timeit
import cProfile

def isPrime(n):
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

def countCircularPrimes(limit):
    count = 4
    circular_primes = set([2,3,5,7])
    for i in range(11, limit + 1, 6):
        for n in [i,i+2]:
            s = str(n)
            if '2' in s or '4' in s or '5' in s or '6' in s or '8' in s or '0' in s:
                continue
            else:
                circs = circular_numbers(s)
                skip = False
                for c in circs:
                    if c in circular_primes:
                        skip = True
                        break
                if skip:
                    circular_primes.update(set(circs))
                    count += 1
                    continue
                else:
                    isCircPrime = True
                    for c in circs:
                        # if not isPrime(int(c)):
                        if not isPrime(c):
                            isCircPrime = False
                            break
                    if isCircPrime:
                        circular_primes.update(set(circs))
                        count += 1
    return count, circular_primes
    
def circular_numbers(s):
    for i in xrange(len(s)):
        yield int(s[i+1:]+ s[:i+1])
    
def gen_combos(minL,maxL,choices):
	cache = {1:choices}
	for length in xrange(2,maxL+1):
		new_chunks = []
		old_chunks = cache[length-1]
		for c in choices:
			for chunk in old_chunks:
				new_chunks.append(c+chunk)
		cache[length] = new_chunks
	results = []
	for k in cache:
		if minL <= k <= maxL:
			results.extend(cache[k])
	return results

def main():
    count = 4
    circular_primes = set([2,3,5,7])
    combos = gen_combos(2,6,['1','3','7','9'])
    for s in combos:
        n = int(s)
        if n in circular_primes:
            count += 1
            continue
        circularPrime = True
        for c in circular_numbers(s):
            if not isPrime(c):
               circularPrime = False
               break
        if circularPrime:
            circular_primes.update(set(circular_numbers(s)))
            count += 1
    return count
 
if __name__ == '__main__':
    # count,circs = countCircularPrimes(1000000)
    # print count
    # t = timeit.Timer('countCircularPrimes(1000000)','from __main__ import countCircularPrimes')
    # print 'Time:', t.timeit(1)
    print main()
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:', t.timeit(1)
    cProfile.run('main()')