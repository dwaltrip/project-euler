import timeit

def p63():
    c = 0
    for i in xrange(1,50):
        k = 1
        while True:
            z = k**i
            if len(str(z)) == i:
                c += 1
            elif len(str(z)) > i:
                break
            k += 1
    return c
            
if __name__ == '__main__':
    t = timeit.Timer('print p63()','from __main__ import p63').timeit(1)
    print 'Time:',t