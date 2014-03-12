from math import log10
import timeit
         
cache_inc = {10:(9,9), 20:(9,18), 30:(8,26), 40:(7,33), 50:(6,39),
         60:(5,44), 70:(4,48), 80:(3,51), 90:(2,53), 100:(54,54)}
         
cache_dec = {10:(9,9), 20:(2,11), 30:(3,14), 40:(4,18), 50:(5,23),
         60:(6,29), 70:(7,36), 80:(8,44), 90:(9,53), 100:(10,63)}

def num_increasing(n):
    cache_inc = {10:(9,9), 20:(9,18), 30:(8,26), 40:(7,33), 50:(6,39),
         60:(5,44), 70:(4,48), 80:(3,51), 90:(2,53), 100:(54,54)}
    power = int(log10(n))
    for p in range(3,power+1):
        k = 10**(p-1)
        for i in range(2,10):
            prev = cache_inc[(i-1)*k]
            next_part = prev[0] - cache_inc[(i-1)*k/10][0]
            cache_inc[i*k] = (next_part, prev[1] + next_part)
        next = cache_inc[(10**p)-k][1] + 1
        cache_inc[10**p] = (next, next)
    return cache_inc[n][1]
        
def num_decreasing(n):
    power = int(log10(n))
    for p in range(3,power+1):
        k = 10**(p-1)
        s =  cache_dec[2*k/10][0] ## all decreasing numbers between k/10 and 2*k/10
        cache_dec[2*k] = (s + 1, cache_dec[k][1] + s + 1)
        for i in range(3,11):
            prev = cache_dec[(i-1)*k]
            next_part = prev[0] + cache_dec[i*k/10][0]
            cache_dec[i*k] = (next_part, prev[1] + next_part)
    return cache_dec[n][1]
    
def doubles(n):
    power = int(log10(n))
    s = 18
    for p in range(3,power+1):
        s += 9
    return s
    
def non_bouncy(n):
    return (num_increasing(n) + num_decreasing(n) - doubles(n))

## quicker and simpler
def nonbouncy(digit):
    base, next = range(11), [0]*11
    down, both = 0, 9*(digit-1)+10
    for digits in range(digit-1):
        down += base[10] - 1
        for i in range(11):
            next[i] = sum([base[j] for j in range(i+1)])
        base, next = next, [0]*11
    return 2*base[10]+down-both-1
    
if __name__ == '__main__':
    print nonbouncy(100)
    t = timeit.Timer('nonbouncy(100)','from __main__ import nonbouncy')
    print 'Time for one run:',t.timeit(1)
    