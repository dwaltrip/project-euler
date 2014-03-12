from itertools import count
from math import log10
import timeit
import cProfile

def main(LIMIT):
    cache = {}
    stop = None
    p = 1
    for i in count(1):
        k = i**3
        s = ''.join(sorted(str(d) for d in str(k)))
        if s in cache:
            cache[s].append(k)
            if len(cache[s]) == LIMIT and not stop:
                stop = int(s[::-1])
                solution = min(cache[s])
                key = s
        else:
            cache[s] = [k]
        if stop and k > stop:
            # print cache[key]
            return solution
        # if int(log10(k)) > p:
            # p = int(log10(k))
            # print 'new power of 10:', p
            
if __name__ == '__main__':
    answer = main(25)
    print 'answer:', answer
    t = timeit.Timer('main(25)', 'from __main__ import main')
    t1 = t.timeit(1)
    print 'Time:', t1
    # cProfile.run('main(5)')