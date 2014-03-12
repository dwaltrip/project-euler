import time
if __name__ == '__main__':
    time.clock()
    # exponent_combos = {}
    # for a in range(2, 101):
        # for b in range(2, 101):
            # exponent_combos[str(a**b)] = None
    # print len(exponent_combos)
    print len(set(a**b for a in range(2,101) for b in range(2,101)))
    print 'elapsed time:',time.clock()