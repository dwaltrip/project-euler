import time
if __name__ == '__main__':
    time.clock()
    ### my shitty solution is commented out
    # s = 0
    # for i in range(2,300000):
        # if sum(int(d)**5 for d in str(i)) == i:
            # s += i
    # prints
    ### this solution below is super fast
    ### it executes in 0.14 seconds while mine took about 7 seconds
    ### not quite sure how the hell this algorithm works, or how the thought of it
    c=0
    for q in range (0,10):
        for w in range (0,q+1):
            for e in range (0,w+1):
                for r in range (0,e+1):
                    for t in range (0,r+1):
                        for y in range (0,t+1):
                            v= (q**5+w**5+e**5+r**5+t**5+y**5)
                            b=0
                            n=str(v)
                            m=0
                            while m < len(n) and b <= v:
                                b+=int(n[m])**5
                                m+=1
                            if b == v :
                                c += v
    print c-1
    print 'time elapsed:', time.clock()