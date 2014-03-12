import math
import timeit
import cProfile

def digit(d):
	p = 0
	while d > 0:
		p += 1
		d -= 9*(10**(p-1))*p
	d += 9*(10**(p-1))*p
	r = d%p-1
	n = int(math.ceil(d*1.0/p))
	return int(str(n+10**(p-1)-1)[r])
    
def main():
    return digit(1) * digit(10) * digit(100) * digit(1000) * digit(10000) * digit(100000) * digit(1000000)

if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:', t.timeit(1)
    cProfile.run('main()')