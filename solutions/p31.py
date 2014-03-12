import time
import timeit

total = 200
a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
if __name__ == '__main__':
    # time.clock()

    ##### algorithm number 1 (my original one) ~~~ 2100 ms
    # s = 0
    # ng = total
    # for _g in range(0, ng/g + 1):
        # n = nf = ng - _g * g
        # for _f in range(0, nf/f + 1):
            # n = ne = nf - _f * f
            # for _e in range(0, ne/e + 1):
                # n = nd = ne - _e * e
                # for _d in range(0, nd/d + 1):
                    # n = nc = nd - _d * d
                    # for _c in range(0, nc/c + 1):
                        # n = nb = nc - _c * c
                        # for _b in range(0, nb/b + 1):
                            # n = na = nb - _b * b
                            # for _a in range(0, na/a + 1):
                                # if na - _a * a == 0:
                                    # s += 1
    # print 'ALG 1', s

    ##### algorithm number 2 (written by me with a little help from the problem 31 thread) ~~~ 1100 ms
    # s = 0
    # for a in range(total, -1, -100):
        # for b in range(a, -1, -50):
            # for c in range(b, -1, -20):
                # for d in range(c, -1, -10):
                    # for e in range(d, -1, -5):
                        # for f in range(e, -1, -2):
                            # for g in range(f, -1, -1):
                                # if g == 0:
                                    # s += 1
    # print 'ALG 2:', s

    ##### algorithm number 3 (copied directly from a post in the problem 31 thread, runs WICKED fast) ~~~ 4.5 ms
    ##### it is 'dynamic programming', or so the person who posted it said
    def nways(n,coins):
        m = len(coins)

        ways = []
        for i in range(n+1):
            ways.append([0 for j in range(m+1)])

        # initialize base cases
        for i in range(n+1):
            ways[i][0] = 0
        for j in range(m+1):
            ways[0][j] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                ways[i][j] += ways[i][j-1]
                if i>=coins[j-1]:
                    ways[i][j] += ways[i-coins[j-1]][j]

        return ways[n][m]
    print 'ALG 3:', nways(total,[1,2,5,10,20,50,100,200])

    ###$$ algorithm number 4 (copied directly from a post also, EVEN FASTER THAN THE ONE ABOVE) ~~~ 2.5 ms
    def ways(amount):
        vals = [1]+[0]*amount
        for coin in [1,2,5,10,20,50,100,200]:
            for i in range(coin,amount+1):
                vals[i] += vals[i-coin]
        return vals[amount]
    t=timeit.Timer("ways(total)", "from __main__ import ways, total")
    print 'ALG 4:', ways(total), '-- elapsed time:', t.timeit(1)

    ##### algorithm number 5 (3rd fastest) ~~~ 12 ms
    # def make_poly( lst ):
        # """
        # Make a polynomial from a range() parameter
        # Expects powers of x; e.g. [1,2,3] is
        # x ** 3 + x ** 2 + x **1
        # returns a hashtable which is power of x -> coefficient
        # """
        # a = {}
        # for i in lst:
            # a[ i ] = 1
        # return a
    # def multiply_poly( a, b ):
        # """ Generate polynomial c from multiplying a and b"""
        # c = {}
        # for exp_i in a:
            # for exp_j in b:
                # coeff_i = a[exp_i]
                # coeff_j = b[exp_j]
                # coeff_existing = c.get( exp_i + exp_j, 0 )
                # c[ exp_i + exp_j ] = coeff_existing + coeff_i * coeff_j
        # return c
    # def calc_31(amount):
        # # coin types
        # polys = [range(0,amount+1,1),
                 # range(0,amount+1,2),
                 # range(0,amount+1,5),
                 # range(0,amount+1,10),
                 # range(0,amount+1,20),
                 # range(0,amount+1,50),
                 # range(0,amount+1,100),
                 # range(0,amount+1,200)]
        # # make a polynomial for each
        # polys = [make_poly( p ) for p in polys]
        # # calculate the product of each
        # result = reduce( lambda x,y: multiply_poly(x,y), polys )
        # # return the coefficient of x ** 200
        # return result[amount]
    # print 'ALG 5:', calc_31(total)

    ##### algorithm 6
    # units = [200,100,50,20,10,5,2,1]
    # def assemble(amt, unitIndex=0):
        # count = 0
        # if amt == 0 or unitIndex==len(units)-1:
            # return 1
        # if amt < 0:
            # return 0
        # for i in xrange(0, amt / units[unitIndex] +1 ):
            # count += assemble( amt - i*units[unitIndex], unitIndex+1)
        # return count
    # t=timeit.Timer("assemble(total)", "from __main__ import assemble, total")
    # print 'ALG 6:', assemble(total), '-- elapsed time:', t.timeit(1)

    # print 'time elapsed:', time.clock()


print "Hello"