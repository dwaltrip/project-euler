import timeit

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


def right_triangle_solutions(p):
	upper_lim = (p - 1)/2
	lower_lim = (p + 1)/3
	solutions = 0
	for c in range(upper_lim, lower_lim - 1, -1):
		for b in range(c - 1, c/2 - 1, -1):
			if (p-c-b)**2 + b**2 - c**2 == 0 and p-c-b < b:
				solutions += 1
	return solutions

def main():
    raw_prims = gen_primitives(10000)
    prims = []
    for i in range(len(raw_prims)):
        if sum(raw_prims[i]) <= 1000:
            prims.append(raw_prims[i])
    cache = [0]*1000
    perims = [sum(p) for p in prims]
    for p in perims:
        for i in range(1, 1000/p + 1):
            cache[p*i - 1] += 1
    # for i,p in enumerate(perims):
        # if p > 0:
            # print i+1,'--',p
    print perims.index(max(perims)) + 1
    
def main2():
    highest, index = 0, 0
    for i in range(12,1001,2):
        current = right_triangle_solutions(i)
        if current > highest:
            highest, index = current, i
    print index,'--',highest
    
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
        

if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:',t.timeit(1)