A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
# A= '1415926535'
# B= '8979323846'

fib_words = [A,B]

def F(n):
    if len(fib_words) > n:
        return fib_words[n]
    else:
        f = F(n-2) + F(n-1)
        fib_words.append(f)
        return f
        
def D(n):
    i = 0
    while True:
        f = F(i)
        if len(f) >= n:
            return f[n-1],f
        i += 1
        
if __name__ == '__main__':
    L = []
    for n in range(1,18):
        L.append((10**n)*(D((127+19*n)*(7**n))))
    print sum(L)
    
###### this solution should work, but python errors out due to memory constraints