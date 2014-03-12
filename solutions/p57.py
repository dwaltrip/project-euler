from math import log10
import timeit

def main():
    n,d,count = 1,2,0
    for i in xrange(999):
        n,d = d,n + 2*d
        if int(log10(n+d)) > int(log10(d)):
            count += 1
    return count
  
if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t