def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def R(d):
    r = 0
    for n in range(1,d):
        if gcd(n,d) == 1:
            r += 1
    return (r*1.0)/(d-1)

def main():
    target = 15499.0 / 94744
    # target = 4.0 / 10
    r = n =1
    while r >= target:
        n += 1
        r = R(n)
        if n % 1000 == 0:
            print n
    print n

def isPrime(n):
    if n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = n**.5
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True
   
def primes():
    for n in [2,3]:
		yield n
    s = 6
    while True:
		if isPrime(s-1):
			yield s-1
		if isPrime(s+1):
			yield s+1
		s += 6
    
def prime_list(limit):
    for p in primes():
        print p
        if p > limit:
            return
        
def divisors(n):
    if n < 2:
        return 1
    count = 0
    divs = {}
    for d in primes():
        while n % d == 0:
            n /= d
            divs[d] = divs[d] + 1 if d in divs else 1
            count += 1
        if n == 1:
            break
    return count
        
# if __name__ == '__main__':
