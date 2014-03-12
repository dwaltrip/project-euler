import timeit
import cProfile
    
def p33():
    fractions = []
    for a in xrange(12,99):
        s = str(a)
        k = int(s[1])*10
        if s[0] == s[1]:
            continue
        else:
            for i in xrange(1,10):
                b = k + i
                if a*1.0/b == (a/10)/(i*1.0):
                    fractions.append((a,b))
    k = 1
    for f in fractions:
        k *= f[0]*1.0/f[1]
    return 1.0/k
    
if __name__ == '__main__':
    t = timeit.Timer('print p33()','from __main__ import p33').timeit(1)
    print 'Time:', t
    cProfile.run('p33()')