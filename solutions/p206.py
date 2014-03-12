from math import ceil, floor, sqrt
import re
import timeit
import cProfile

MIN = 1020304050607080900
MAX = 1929394959697989990
# simple_test = set('123456789')

# def main():
    # pattern = re.compile(r'1\d2\d3\d4\d5\d6\d7\d8\d9\d0')
    # start = int(ceil(sqrt(MIN)))
    # start = start + 100 - start % 100
    # stop = int(floor(sqrt(MAX)))
    # t = start
    # while t < stop:
        # for i in [t-30, t-70]:
            # k = i**2
            # if pattern.findall(str(k)):
                # return i
        # t += 100
        
# def main2():
    # start = int(ceil(sqrt(MIN)))
    # start = start + 100 - start % 100
    # stop = int(floor(sqrt(MAX)))
    # digit_check = [8,7,6,5,4,3,2,1]
    # t = start
    # while t < stop:
        # for n in [t-30, t-70]:
            # k = n**2
            # i, power = 0, 5
            # found_it = False
            # while True:
                # div = 10**(power-1)
                # digit = ((k % (div * 10)) - (k % div)) / div                
                # if digit_check[i] != digit:
                    # break
                # i += 1
                # power += 2
                # if i > 7:
                    # found_it = True
                    # break
            # if found_it:
                # return n
        # t += 100
        
def main3():
    start = int(ceil(sqrt(MIN)))
    start = start + 100 - start % 100
    stop = int(floor(sqrt(MAX)))
    digit_check = [8,7,6,5,4,3,2,1]
    t = start
    while t < stop:
        for n in [t-30, t-70]:
            s = str(n**2)
            if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8':
                return n
        t += 100

if __name__ == '__main__':
    print main3()
    t = timeit.Timer('main3()', 'from __main__ import main3')
    print 'Time:', t.timeit(1)
    cProfile.run('main3()')
    
# def matches_pattern(n, length):
    # match = 0
 
    # for i in range(0, (length+1)/2):
        # if n % 10 != match:
            # return False
        # match = (match - 1) % 10
        # n /= 100
 
    # return True
 
# def try_it(sol):
    # length = len(sol)
 
    # if length == 10:
        # square = int(sol)*int(sol)
        # if len(str(square)) > 19 or not matches_pattern(square, 19):
            # return None
 
        # return sol
 
    # for new_digit in range(0, 10):
        # new_sol = str(new_digit) + sol
        # new_square = int(new_sol)*int(new_sol)
        # if matches_pattern(new_square, length+1):
            # result = try_it(new_sol)
            # if result != None:
                # return result
 
    # return None
 
# print try_it('')
# import timeit
# t = timeit.Timer('try_it("")','from __main__ import try_it')
# print 'Time:', t.timeit(1)
# import cProfile
# cProfile.run('try_it("")')