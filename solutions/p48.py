import datetime
import timeit

t1 = datetime.datetime.now()
sol_1 = str(sum(i**i for i in range(1,1001)))[-10:]
t2 = datetime.datetime.now()

t3 = datetime.datetime.now()
sol_2 = sum(i**i for i in range(1, 1001)) % 10**10
t4 = datetime.datetime.now()

t5 = datetime.datetime.now()
sol_3 = 0
for n in xrange(1, 1001):
    sol_3 = (sol_3 + (n ** n)) % 10000000000
t6 = datetime.datetime.now()

# print 'Solution 1:',sol_1,'Time:',t2-t1
# print 'Solution 2:',sol_2,'Time:',t4-t3
# print 'Solution 3:',sol_3,'Time:',t6-t5
t1 = timeit.Timer('sol_1 = str(sum(i**i for i in xrange(1,1001)))[-10:]')
print 'Solution 1:',sol_1,'Time:',t1.timeit(1)
t2 = timeit.Timer('sol_2 = sum(i**i for i in xrange(1, 1001)) % 10**10')
print 'Solution 2:',sol_2,'Time:',t2.timeit(1)
t3 = timeit.Timer('sol_3 = 0\nfor n in xrange(1,1001):\n\tsol_3 = (sol_3 + (n ** n)) % 10000000000')
print 'Solution 3:',sol_3,'Time:',t3.timeit(1)