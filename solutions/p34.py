from math import factorial
import timeit

f = {}
for i in range(10):
    f[str(i)] = factorial(i)

def sfd(n):
    return sum([f[d] for d in str(n)])

def calc():
    s = 0
    for i in range(3,2200001):
        if i == sfd(i):
            s += i
    return s

if __name__ == '__main__':
    print 'Starting timer...'
    t = timeit.Timer('calc()','from __main__ import calc')
    print 'Time:',t.timeit(1)