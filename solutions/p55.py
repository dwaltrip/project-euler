import timeit
    
def main():
    lychrel_count = 0
    for i in xrange(1,10001):
        n = i + int(str(i)[::-1])
        lychrel = True
        for k in xrange(50):
            r = int(str(n)[::-1])
            if not n == r:
                n += r
            else:
                lychrel = False
                break
        if lychrel:
            lychrel_count += 1
    return lychrel_count

if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:',t.timeit(1)