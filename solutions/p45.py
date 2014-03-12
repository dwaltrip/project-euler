from math import sqrt
from itertools import count
from timeit import Timer
import cProfile

def quadratic_solver(a,b,c):
    return (-b + sqrt(b**2 - 4*a*c))/(2*a)
    
def main():
    for n in count(286):
        t = (n*(n+1))/2
        p = (.5 + sqrt(.25 - 6.0*(-t)))/(3.0)
        if p == int(p):
            h = (1.0 + sqrt(1.0 - 8.0*(-t)))/(4.0)
            if h == int(h):
                return t
                
def main2():
    p, pi = 40755, 496
    h, hi = 40755, 573
    while True:
        if p < h:
            p += pi
            pi += 3
        else:
            h += hi
            hi += 4
        if p == h:
            break
    return p

                
if __name__ == '__main__':
    print main2()
    t =  Timer('main2()', 'from __main__ import main2')
    print 'Time:', t.timeit(1)
    cProfile.run('main2()')