from math import ceil, sqrt
from itertools import count
import time

class quadratic(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def eval(self, x):
        return x**2 + self.a*x + self.b

def isPrime(n):
    n = abs(n)
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

## i should find a way to make this faster, it currently takes about 39 seconds to run
if __name__ == '__main__':
    time.clock()
    highest = 0
    c1, c2 = 0, 0
    for a in range(-1000,1000):
        if (a + 1000) % 200 == 0:
            print str((a + 1000)/20) + '% complete!'
        for b in range(-1000,1000):
            q = quadratic(a,b)
            current_count = 0
            c = count()
            while True:
                n = q.eval(c.next())
                if n > 0 and isPrime(n):
                    current_count += 1
                    if current_count > highest:
                        highest, c1, c2 = current_count, a , b
                else:
                    break
    print c1, 'x', c2, '=', c1 * c2, '----', highest
    print 'elapsed time:', time.clock()
