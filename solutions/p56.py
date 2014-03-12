from timeit import Timer

def main2():
    pass
    

def main():
    # return max(sum(int(d) for d in str(num)) for num in [a**b for a in xrange(1,100) for b in xrange(1,100)])
    return max(sum(int(d) for d in str(a**b)) for a in xrange(90,100) for b in xrange(90,100))

if __name__ == '__main__':
    print main()
    t = Timer('main()','from __main__ import main')
    print 'Time:', t.timeit(1)