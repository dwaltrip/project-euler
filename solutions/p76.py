import timeit

def ways(N, values):
   a = [1] + [0]*N
   for v in values:
      for i in xrange(v,N+1):
         a[i] += a[i-v]
   return a[N]

if __name__ == '__main__':
   N = 10000
   s1 = 'print ways(%d, xrange(1,%d))' % (N, N)
   s2 = 'from __main__ import ways'
   t = timeit.Timer(s1,s2).timeit(1)
   print 'Time:', t