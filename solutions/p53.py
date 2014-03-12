import timeit

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
    
def p53():
    LIM = 10**6
    c = 0
    for n in xrange(1,101):
        for k in xrange(1,n/2+1):
            if choose(n,k) > LIM:
                c += (n-k) - k + 1
                break
    return c
    
if __name__ == "__main__":
    t = timeit.Timer('print p53()','from __main__ import p53').timeit(1)
    print 'Time:', t