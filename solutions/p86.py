from math import sqrt

# too tired to keep going, plus gotta do hw
# current GENERAL strategy (for next time i look at this problem):
# generate all right triangles with sides a,b,c of integer length,
# such that a<=M and b<=2*M. Then loop through these triangles,
# setting z=a and x+y=b, where x,y,z represent a cuboid whose shortest path
# between opposing corners is of integer length. We assert that x<=y<=z, and
# thus for any a,b pair we want b<=2*a.  Assuming b<=2*a holds, we set d = abs(b-a),
# and then the possible x-values are:
#		if b > a: {d,d+1,...,(x+y)/2 - 1, (x+y)/2}
#		if a > b: {1,2,...,(x+y)/2 - 1, (x+y)/2}
#	of course, y = b - x
# we can add these x,y,z triplets to a set, and blah blah blah this needs some
# rethinking
    
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def gen_primitives(v):
    prev_len = 0
    while True:
        start = 1 if v % 2 == 0 else 2
        for u in xrange(start, v, 2):
             if gcd(u,v) == 1:
                a,b,c = tuple(sorted((v**2-u**2,2*u*v,u**2+v**2)))
                if b > 2*lim:
                    break
                else:
                    PRIMITIVES[(a,b)] = c
                    RIGHT_TRIANGLES[(a,b)] =c
                    newly_added[(a,b)] = c
        if prev_len == len(newly_added):
            return
        prev_len = len(newly_added)
	v += 1
        V[1] += 1
    
def add_multiples(M):
    for a_b,c in PRIMITIVES.iteritems():
        m = M/c
        a,b = a_b
        for i in xrange(2,m+1):
            RIGHT_TRIANGLES[(a*i, b*i)] = c*i            
    
def p86():
    goal = 10**6
    M = 100
    gen_primitives(V[1],M,{})
    add_multiples(100)
    sols = []
    for a_, b_ in RIGHT_TRIANGLES.iterkeys():
	for a, b in [(a_, b_),(b_, a_)]:
	    if b > 2*a:
		continue
	    else:
		start = 1 if a > b else b - a
		for x in xrange(1,b/2+1):
		    sols.append((x,b-x,a))
		
    print len(sols)
    sols2 = [(a,b,c) for a,b,c in sols if c <= M]
    print len(sols2)
    f = open('c:\\pythonwork\\p86.txt','w')    
    for s in sorted(sols):
	f.write(str(s)+'\n')
    f.close()
    #sols = 2060
    #while sols < goal:
    #    M += 1
    #    s = 0
    #    newly_added = {}
    #    gen_primitives(V[1],2*(M-1),newly_added)
    #    for x, y_plus_z in RIGHT_TRIANGLES.iterkeys():
    #        if 2*x > y_plus_z:
    #            continue
    #        else:
    #            for y in xrange(x, y_plus_z / 2 + 1):
    #                s += 1
    #    sols += s
    #return M
    
V = {1:2}
SOLUTIONS = set()
PRIMITIVES = {}
RIGHT_TRIANGLES = {}
if __name__ == '__main__':
    p86()