import timeit

def p81():
    lines = open('c:\\pythonwork\\project_euler\\matrix.txt').readlines()
    values = [[int(s) for s in line.split(',')] for line in lines]
    first_row = values[0]
    rows, cols = len(values), len(first_row)
    m = [[sum(first_row[:i]) for i in xrange(1,cols+1)]]
    for i in xrange(1,rows):
        m.append([0 for i in xrange(cols)])
    for j in xrange(1,rows):
        for i in xrange(cols):
            if i>0 and m[j][i-1] < m[j-1][i]:
                m[j][i] = m[j][i-1] + values[j][i]
            else:
                m[j][i] = m[j-1][i] + values[j][i]
    return m[rows-1][cols-1]
    
if __name__ == '__main__':
    t = timeit.Timer('print p81()','from __main__ import p81').timeit(1)
    print 'Time:',t