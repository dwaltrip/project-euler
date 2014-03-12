from itertools import count
from timeit import Timer
import cProfile

factorials = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}

cache = {0:[0]}
def increasing_nums(start=1, stop=None, cache=None):
    if not cache:
        cache = {0:[0]}
        p = 1
    else:
        p = max(cache.keys()) or 1
    done = False
    while True:
        temp = []
        for k in cache[p - 1]:
            lb = k % 10 or 1
            for d in xrange(lb, 10):
                n = k * 10 + d
                if stop and n >= stop:
                    done = True
                temp.append(n)
                if n >= start:
                    yield n
        cache[p] = temp
        p += 1
        if done:
            return

# def f(n):
    # s = str(n)
    # return sum(factorials[d] for d in s)
    
# def sf(n):
    # s = str(f(n))
    # return sum(int(d) for d in s)
    
def sf(n):
    s1 = str(n)
    s2 = str(sum(factorials[d] for d in s1))
    return sum(int(d) for d in s2)

N = 1
G = {} 
def g(n):
    global N
    if n in G:
        return G[n]
    else:
        for i in increasing_nums(start=N, cache=cache):
            k = sf(i)
            if k == n:
                N = i + 1
                return i
            else:
                if k not in G:
                    G[k] = i
            
def sg(n):
    s = str(g(n))
    return sum(int(d) for d in s)
    
def ds(n):
    s = str(n)
    return sum(int(d) for d in s)
    
def main(n):
    total = []
    for i in xrange(1,n+1):
        total.append((i,g(i)))
        if i%(n/10) == 0:
            print str(10*i / (n/10)) + '% complete!'
    print 'N:', N-1
    print 'answer:', sum(ds(n) for i,n in total)
    print total
    print
    # s = 0
    # for i in xrange(1,n+1):
        # s += sg(i)
        # if i%(n/10) == 0:
            # print str(10*i / (n/10)) + '% complete!'
    # return s
    
NN = 50
    
if __name__ == '__main__':
    # main(NN)
    # tt = Timer('main(NN)','from __main__ import main,NN')
    # t = tt.timeit(1)
    # print 'Time:', t
    cProfile.run('main(NN)')