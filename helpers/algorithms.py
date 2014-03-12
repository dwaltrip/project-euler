def combos(n,values):
	'''returns a list of all n-sized combinations of the elements in values'''
	if n==1:
		return [[v] for v in values]
	lst = []
	for i,v in enumerate(values):
		for c in combos(n-1,values[i+1:]):
			lst.append([v]+c)
	return lst

def choose(n, k):
    if k > n:
        return 0
    if k > n/2:
        k = n - k
    accum = 1
    for i in xrange(1, k+1):
        accum *= (n-k+i)
        accum /= i
    return accum

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def get_digit(num, digit):
	'''returns the nth digit, counting from the right side of the number,
	where n is specified through the "digit" parameter'''
	k = 10**(digit-1)
	return ((num % (k*10)) - (num % k)) / k
	
def gen_char_and_rest(chars):
    for i in xrange(len(chars)):
        yield (chars[i], chars[:i] + chars[i+1:])

def prime_factors(n):
    pf = defaultdict(lambda: 0)
    primes = gen_primes()
    p = primes.next()
    while n > 1:
        while n%p == 0:
            n /= p
            pf[p] += 1
        p = primes.next()
    return pf

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

def block_comment():
	def gen_primes():
	    """ Generate an infinite sequence of prime numbers."""
	    # Maps composites to primes witnessing their compositeness.
	    # This is memory efficient, as the sieve is not "run forward"
	    # indefinitely, but only as long as required by the current
	    # number being tested.
	    
	    from collections import defaultdict
	    D = defaultdict(list)
	    
	    # The running integer that's checked for primeness
	    q = 2  
	
	    while True:
	        if q not in D:
	            # q is a new prime.
	            # Yield it and mark its first multiple that isn't
	            # already marked in previous iterations
	            # 
	            yield q        
	            D[q * q] = [q]
	        else:
	            # q is composite. D[q] is the list of primes that
	            # divide it. Since we've reached q, we no longer
	            # need it in the map, but we'll mark the next 
	            # multiples of its witnesses to prepare for larger
	            # numbers
	            # 
	            for p in D[q]:
	                D[p + q].append(p)
	            del D[q]
	            
	        q += 1
	return None
        
def gen_primes():
    """ Generate an infinite sequence of prime numbers."""
    from collections import defaultdict
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
    
def gen_perms(chars):
	if len(chars)<=1:
		yield chars
	else:
		for p in gen_perms(chars[1:]):
			for i in xrange(len(p)+1):
				yield p[:i] + chars[0] + p[i:]

def gen_ordered_perms(chars):
	char_list = sorted(chars)
	if len(char_list)==2:
		yield ''.join(char_list)
		yield ''.join(char_list[::-1])
	else:
		for i,c in enumerate(char_list):
			sub_list = char_list[:i] + char_list[i+1:]
			for new_str in gen_permutations(sub_list):
				yield c + new_str
    
def for_loops(digits, limit):
    # 'status' represents all of the variables from every loop except the innermost one
    # we initialize it with all values equal to 0
    status = [0]*(digits-1)
    while True:
        # this is the innermost loop
        for i in xrange(limit):
			for k in xrange(1,digits):
				i += status[-k]*10**k
			yield i
        c = 0
        while status[c] == limit - 1:
			c += 1
            # this is the stopping condition for finishing all of the nested for loops
            # we are done when every variable in the 'status' array is equal to limit - 1
            # if limit = 10, digits = 5, we are done when status looks like [9, 9, 9, 9]
			if c == digits - 1:
				return
        # adjust the 'status' array everytime the innermost loops does a complete run through
        # find the value closest to the end of the 'status' array that is less than limit - 1, and increment it by 1
        # and then set every value to the right of that value equal to 0
        t = -1
        while status[t] == limit - 1:
			t -= 1
        status[t] += 1
        for s in xrange(t+1,0):
			status[s] = 0
          
def increasing_digits(start=1, stop=None):
    digits = []
    for d in str(start):
        digits.append(int(d))
    for i in xrange(1,len(digits)):
        if digits[i] < digits[i-1]:
            digits[i] = digits[i-1]
    last_digit = digits.pop()
    while True:
        for i in xrange(last_digit,10):
            n = int(''.join(str(d)for d in digits + [i]))
            if stop and n > stop:
                return
            yield n
        k = 1
        num_digits = len(digits)
        while not digits or digits[-k] == 9:
            k += 1
            if k == num_digits + 1 or not digits:
                digits = [1] * (num_digits + 1)
                break
        else:
            digits[-k] += 1
            for i in xrange(-k+1,0):
                digits[i] = digits[-k]
        last_digit = digits[-1]
        
def increasing_cache(start=1, stop=None):
    cache = {0:[0]}
    p = 1
    while True:
        temp = []
        for k in cache[p - 1]:
            lb = k % 10 or 1
            for d in xrange(lb, 10):
                n = k * 10 + d
                if stop and n >= stop:
                    return
                temp.append(n)
                if n >= start:
                    yield n
        cache[p] = temp
        p += 1
            
from itertools import product
def n_loops(digits, limit):
	args = [xrange(limit) for i in xrange(digits)]
	for vals in product(*args):
		s = ''.join(str(v) for v in vals)
		yield int(s)
        
def nested_loops(items):
        def _outer_product(depth, current):
            if depth == 1:
                return (current + [elem] for elem in items[-depth])
            else:
                return (res 
                        for elem in items[-depth]
                        for res in _outer_product(depth - 1, current + [elem]))
        if items:
            return _outer_product(len(items), [])
        else:
            return []
            
def nested_xrange(digits, limit):
    args = [xrange(limit) for i in xrange(digits)]
    for n in nested_loops(args):
        yield n

def loop(action, values, *args):
    if values is None:
        values = []
    if args:
        for value in args[0]:
            loop(action, values + [value], *args[1:])
    else:
        return action(*values)

def action(*values):
    yield values
        
def m5():
    s = 0
    for i in loop(action, None, xrange(10), xrange(10)):
        s += 1
    print s
        
def m1():
    s = 0
    for n in for_loops(7,10):
        s += 1
    # print s
    
def m2():
    s = 0
    for n in n_loops(5,10):
        s += 1
    print s

def m3():
    s = 0
    for n in nested_xrange(7,10):
        s += 1
    # print s
    
def m4():
    data = []
    for i in for_loops2(12,10):
        data.append(i)
    return data
        
# def apply_all(action, iterable):
    # for elem in iterable:
        # action(elem)

# def action(elem):
    # print elem
    
class NumDigits(object):
    def __init__(self):
        self.powers_complete = 1
        self.cache = {0:1, 1:10}
        
    def how_many(self, n):
        p = int(log10(n))
        if p + 1 > self.powers_complete:
            self.build_cache(p+1)
        return self.cache[p] + (p + 1)*(n + 1 - (10**p))
        
    def build_cache(self, max_p):
        for p in xrange(self.powers_complete + 1, max_p + 1):
            self.cache[p] = self.cache[p-1] + 9*p*(10**p-1)
        self.powers_complete = max_p
    
import timeit    
if __name__ == '__main__':
    # t3 = timeit.Timer('m3()','from __main__ import m3')
    # tt3 = t3.timeit(1)
    # print 'Time for method m3:', tt3
    # t1 = timeit.Timer('m1()','from __main__ import m1')
    # tt1 = t1.timeit(1)
    # print 'Time for method m1:', tt1
    t5 = timeit.Timer('m5()','from __main__ import m5')
    tt5 = t5.timeit(1)
    print 'Time for method m5:', tt5
    