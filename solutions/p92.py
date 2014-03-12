from math import factorial
from collections import defaultdict
import timeit
import cProfile

SQUARES = {'0':0, '1':1, '2':4, '3':9, '4':16, '5':25, '6':36, '7':49, '8':64, '9':81}

# def ssd(s):
	# return sum(SQUARES[d] for d in s)
    
def ssd(n):
	sum = 0
	while (n > 0):
		sum += (n%10)*(n%10)
		n /= 10
	return sum
   
# def main():
    # count = 0
    # cache1 = set()
    # cache89 = set()
    # for i in xrange(1,10000001):
        # n = i
        # path = []
        # while True:
            # if n == 1 or n in cache1:
                # cache1.update(path)
                # break
            # elif n == 89 or n in cache89:
                # cache89.update(path)
                # count += 1
                # break
            # else:
                # path.append(n)
                # n = ssd(n)
        # if i % 1000000 == 0:
            # print str(i / 100000) + '% complete!'
    # return count
    
# def main2():
    # cache = {}
    # for i in xrange(1, 568):
        # k = i
        # while k != 1 and k != 89:
            # k = ssd(k)
        # cache[i] = k
    # count = 0
    # print 'Starting real loop'
    # for i in xrange(2,10000001):
        # if cache[ssd(i)] == 89:
            # count += 1
        # if i % 1000000 == 0:
            # print str(i / 100000) + '% complete!'
    # return count
    
# def permute(n): # the number of permutations of n
    # x = set(n)
    # y = factorial(len(n))
    # n = list(n)
    # for a in x:
        # y = y/factorial(n.count(a))
    # return (y)
    
def permute(s):
    p = factorial(len(s))
    digits = {}
    for d in s:
        if d in digits:
            digits[d] += 1
        else:
            digits[d] = 1
    for count in digits.itervalues():
        p /= factorial(count)
    return p
    
## this runs in half a second..
## the algorithm that I wrote completely by myself ran in 360 seconds, and then 90 after a few improvements... argh lol
def main3():
    cache = {0:1}
    for i in xrange(1, 568):
        k = i
        while k != 1 and k != 89:
            k = ssd(k)
        cache[i] = k
    count = 0
    for d1 in xrange(0,10):
        for d2 in xrange(d1,10):
            for d3 in xrange(d2,10):
                for d4 in xrange(d3,10):
                    for d5 in xrange(d4,10):
                        for d6 in xrange(d5,10):
                            for d7 in xrange(d6,10):
                                s = ''.join([str(d1),str(d2),str(d3),str(d4),str(d5),str(d6), str(d7)])
                                # s = ''.join(map(str,[d1,d2,d3,d4,d5,d6,d7]))
                                if cache[int(ssd(s))] == 89:
                                    count += permute(s)
    return count
          
if __name__ == '__main__':
    print main3()
    t = timeit.Timer('main3()', 'from __main__ import main3')
    tt = min(t.repeat(5,1))
    print 'Time:', tt
    cProfile.run('main3()')

# def exprime(n):
  # if n == 0:
     # exa[0] = 1
     # return 1
  # exa[n] = n*exprime(n-1)
  # return exa[n]
 
# def ex(n):
   # return exa[n]
 
# def recur(s, digit, r):
   # for count in range(r, -1, -1):
      # thestr = s + str(digit)*count
      # remain = r - count
      # if ((digit < 9) and (remain > 0)):
         # recur(thestr, digit+1, remain)
      # else:
         # if (thestr):
            # p.append(int(thestr))
 
# def dsum(n):
    # return(sum(int(x)**2 for x in str(n)))                               
 
# def mcoef(n,p):
  # s = str(n)
  # return ex(p) / reduce(lambda x,y: x*ex(y), [ex(p - len(s))] + [s.count(x) for x in set(s)])
 
# def ncheck(n, maxs):
   # if (n < maxs):
      # if (d[n] > 0):
         # return d[n]
   # t = ncheck(dsum(n), maxs)
   # if (n < maxs):
      # d[n] = t
   # return t
 
# def calculate(n):
   # maxsum = 81*n + 1
   # if (len(exa) <= max(n,9)):
      # exa.extend([0]*(max(n,9) + 1 - len(exa)))
   # if (len(d) < maxsum):
      # d.extend([0]*(maxsum - len(d)))
      # d[1] = 1
      # d[89] = 89
   # recur('', 1, n)
   # ignore = exprime(max(n,9))
   # total = 0
   # while (p):
      # x = p.pop()
      # t = ncheck(x,maxsum)
      # if (t == 89):
         # total += mcoef(x,n)
   # return total
 
# d,p,exa = [],[],[]
# def main():
    # return calculate(7)