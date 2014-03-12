from math import log
import timeit

def main():
    f = open('c:\\pythonwork\\project_euler\\base_exp.txt', 'r')
    highest = line_num = 0
    for i, line in enumerate(f.readlines()):
        base,exp = map(int, line.strip('\n').split(','))
        current = exp*log(base)
        if current > highest:
            highest = current
            line_num = i+1
    return line_num
    
if __name__ == '__main__':
        print main()
        t = timeit.Timer('main()', 'from __main__ import main')
        print 'Time:', t.timeit(1)