from itertools import combinations

VALID = set(['01','04','0X','1X','25','3X','4X','X4','81'])

def check(d1, d2, debug=False):
    d1 = [s if s not in '69' else 'X' for s in d1]
    d2 = [s if s not in '69' else 'X' for s in d2]

    if debug:
        print 'd1 adjusted: \t%s' % (str(d1))
        print 'd2 adjusted: \t%s' % (str(d2))

    s = set()
    for s1 in d1:
        for s2 in d2:
            s.add(s1+s2)
            s.add(s2+s1)
    if VALID.issubset(s):
        return True
    return False

def main():
    c = 0
    sets = list(combinations(['0','1','2','3','4','5','6','7','8','9'],6))
    print len(sets)
    print '-----'

    for d1 in sets:
        for d2 in sets:
            if check(d1,d2):
                c += 1
            # 831 has no specific significance, it is simply roughly the right magnitude and not even/'nice'
            #if c % 831 == 0:
            #    print '============'
            #    print 'd1: \t\t%s' % (str(d1))
            #    print 'd2: \t\t%s' % (str(d2))
            #    check(d1, d2, debug=True)

    return c

if __name__ == "__main__":
    print main()/2 # divide by two because we are double counting each possibility
