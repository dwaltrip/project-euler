import timeit
import math
import cProfile
import pstats
from itertools import count

def palindromes(limit=None, length=None):
	if limit is not None:
		range = xrange(1, min(10, limit+1))
	else:
		range = xrange(1, 10)
 
	for i in range:
		yield i 
 
	for digits in count(2):
		lower = 10 ** ((digits // 2) - 1)
		upper = (10 ** (digits // 2)) - 1 
 
		for i in xrange(lower, upper + 1):
			text = str(i)
 
			if digits % 2 == 0:
				number = int("%s%s" % (text, text[::-1]))
 
				if number <= limit:
					yield number
				else:
					return
			else:
				for x in xrange(10):
					number = int("%s%s%s" % (text, x, text[::-1]))
 
					if number <= limit:
						yield number
					else:
						return

### older crappy way
# def palindromeList(limit):
    # palindromes = {1:set(['0','1','2','3','4','5','6','7','8','9']), 2:set(['00','11','22','33','44','55','66','77','88','99'])}
    # power = int(math.log10(limit))
    # for p in xrange(3,power+1):
        # palindromes[p] = set()
        # for n in xrange(10**(p-1),10**p + 1):
            # s = str(n)
            # if s[0] == s[p-1] and s[1:p-1] in palindromes[p-2]:
                # palindromes[p].add(s)
    # results = set()
    # for subset in palindromes.values():
        # results.update(subset)
    # return results
    
## super duper fast, designed by me!!
## not completely accurate, it misses some of the ones where zeros are inserted into the palindromic pattern
def palindromeList(limit):
    palindromes = {1:[0,1,2,3,4,5,6,7,8,9], 2:[0,11,22,33,44,55,66,77,88,99]}
    power = int(math.ceil(math.log10(limit)))
    for p in xrange(3, power+1):
        next = []
        k = 10**(p-1)
        for i in xrange(1,10):
            for bit in palindromes[p-2]:
                next.append(i*k + bit*10 + i)
        if p > 4:
            for z in xrange(4,p,2):
                for i in xrange(i,10):
                    for bit in palindromes[p-z]:
                        next.append(i*k + bit*(10**(z/2)) + i)
        palindromes[p] = next
    results = []
    for subset in palindromes.values():
        results.extend(subset)
    results.remove(0)
    results.remove(0)
    return results

def isBase10_Palindrome(n):
    s = str(n)
    return s == s[::-1]
	# l = len(s)
	# for i in xrange(l/2):
		# if s[i] != s[l-i-1]:
			# return False
	# return True
    
def isBase2_Palindrome(n):
    s = bin(n)[2:]
    return s == s[::-1]
	# l = len(s)
	# for i in xrange(l/2):
		# if s[i] != s[l-i-1]:
			# return False
	# return True
    
def isPalindrome(n, base=10):
	r,k = 0,n
	while k > 0:
		r = r*base + k%base
		k /= base
	if r == n:
		return True
	return False
    
def main(limit):
    palindromes = palindromeList(limit)
    s = 0
    pals = []
    for p in palindromes:
        if isBase2_Palindrome(p):
            s += p
            pals.append(p)
    return pals
    
def makePalindrome(n,base,oddlength):
    res = n
    if oddlength: n /= base
    while n > 0:
        res = base*res + n%base
        n /= base
    return res
    
def makePalindromeBase2(n,oddlength):
    res = n
    if oddlength: n >>= 1
    while n > 0:
        res = (res << 1) + (n & 1)
        n >>= 1
    return res

def main2(limit):
    s = 0
    i = 1
    # pals = []
    p = makePalindromeBase2(i,True)
    while p < limit:
        if isBase10_Palindrome(p):
            s += p
            # pals.append(p)
        i += 1
        p = makePalindromeBase2(i,True)
    i = 1
    p = makePalindromeBase2(i,False)
    while p < limit:
        if isBase10_Palindrome(p):
            s += p
            # pals.append(p)
        i += 1
        p = makePalindromeBase2(i,False)
    return s
    
def test(limit):
    pals = []
    for p in palindromes(limit):
        pals.append(p)
    return pals
    
if __name__ == '__main__':
    # print main2(10**9)
    # t = timeit.Timer('main2(10**9)', 'from __main__ import main2')
    # print 'Time:',t.timeit(1)