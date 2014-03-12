import time
def diag_sum(num):
    if (num - 1) % 2 != 0:
        num -= 1
    x = [1]
    i = 2
    prev = 1
    while x[len(x)-1] < num**2:
        x.extend([prev + i, prev + 2*i, prev + 3*i, prev + 4*i])
        prev += 4*i
        i += 2
    return sum(x)

if __name__ == '__main__':
    time.clock()
    print diag_sum(1001)
    print 'elapsed time:', time.clock()