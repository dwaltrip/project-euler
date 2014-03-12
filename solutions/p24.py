from math import factorial
from timeit import Timer

def nlp(n, chars):
    """
    calculates the Nth Lexigraphical Permutation
    for a string of characters.
    """
    if factorial(len(chars)) < n: return False
    chars = sorted(list(chars))
    sol = ''
    for i in range(len(chars)-1,-1,-1):
        f = factorial(i)
        if f > n:
            sol += chars.pop(i)
        else:
            d = n / f - 1 if n % f == 0 else n / f
            sol += chars.pop(d)
            n = n - d * f
    return sol
    
if __name__ == '__main__':
    print nlp(1000000,"0123456789")
    t = Timer('nlp(1000000,"0123456789")', 'from __main__ import nlp')
    print 'Time:', t.timeit(1)