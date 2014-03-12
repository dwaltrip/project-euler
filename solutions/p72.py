from math import ceil, sqrt

def is_prime(n):
   if n == 1:
      return False
   for i in xrange(2, int(ceil(sqrt(n))) + 1):
      if n % i == 0:
         return False
   return True

primes = [i for i in xrange(1, 1001) if is_prime(i)]

print len(primes)
print primes
print "~~~"

def get_multiples_less_than(num_list, limit):
   
   
def count_proper_fractions(max_denom):
   count = 0
   for d in xrange(2, max_denom + 1):
      i = 0
      p = primes[i]
      k = int(ceil(sqrt(d)))
      while p < k:
         i = i + 1
         p = primes[i]
         count = count + 1
   print count
         
#count_proper_fractions(1000)
#count_proper_fractions(10000)
#count_proper_fractions(100000)
#count_proper_fractions(1000000)