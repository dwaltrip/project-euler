import timeit

def main():
    standard = set('123456789')

    for i in xrange(9999,8999,-1):
       temp = str(i)+str(i*2)
       if len(temp) == 9 and set(temp) == standard:
           return temp
    else:
       return 'loop finished, no results'
       
if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main').timeit(1)
    print 'Time:', t