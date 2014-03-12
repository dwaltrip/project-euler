

def gen_primitives(lim):
	prims = []
	v = 2
	while True:
		if v % 2 == 0:
			start = 1
		else:
			start = 2
		p = 0
		exit = False
		for u in range(start, v, 2):
			if gcd(u,v) == 1:
				a,b,c = v**2-u**2,2*u*v,u**2+v**2
				prims.append(sorted([a,b,c]))
				p = a+b+c
			if p > lim:
				exit = True
				break
		if exit:
			break
		v += 1
	return prims
    
def count_primitives(lim):
	prims = []
	v = 2
    c = 0
    while True:
		if v % 2 == 0:
			start = 1
		else:
			start = 2
		p = 0
		exit = False
		for u in xrange(start, v, 2):
			if gcd(u,v) == 1:
				a,b,c = v**2-u**2,2*u*v,u**2+v**2
				c += 1
				p = a+b+c
			if p > lim:
				exit = True
				break
		if exit:
			break
		v += 1
	return c

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
if __name__ == "__main__":
    print count_primitives(10**6)