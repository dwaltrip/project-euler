import timeit

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def main():
    count = 0
    for i in xrange(1,12001):
        lb, ub, step = (i-1)/3, (i+1)/2, 1
        if i % 2 == 0:
            lb -= 1 if lb % 2 == 0 else 0
            step = 2
        for j in xrange(lb, ub, step):
            if gcd(i,j) == 1 and 1.0/3 < (1.0*j)/i < 1.0/2:
                count += 1
    return count
    
def main3():
    f = {}
    for d in range(12001):
        for a in range(d/3+1,d/2+1):
            if (1.0*a/d != 0.5):
                f[1.0*a/d] = 1
    return len(f)
    
def farey(max, d1, d2):
   count = 0
   li = [0]
   while d2 != 0:
     if d1 + d2 <= max:
       li.append(d2)
       d2 = d1 + d2
       count = count + 1
     else:
       d1 = d2
       d2 = li.pop()
   return count    
    
####### way faster than anything else, the kid who wrote this is a genius
def calc_less_than(x, n):
  #a[q] - number irreducible fractions less than x whith denominator equal to q
  a = [int(q*x) for q in xrange(n+1)]
  for q in xrange(1, n+1):
    m = 2
    while(m*q<=n):
      a[m*q] -= a[q]
      m += 1
  return sum(a)-1
  
def main4():
    return calc_less_than(0.5,12000)-calc_less_than(1./3,12000)-1
 
if __name__=='__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t