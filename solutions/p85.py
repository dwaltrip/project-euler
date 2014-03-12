import timeit
from math import sqrt

#my relatively smart way
def count_rects(num_rows, num_cols):
    a = min((num_rows,num_cols))
    b = max((num_rows,num_cols))
    m = (b*(b+1))/2
    return sum(m*k for k in xrange(1,a+1))

# from the problem 85 forum:
# There is an analytical way to solve this one.
# If you imagine a rectangular grid measuring a units across and b units down.
# There are a+1 vertical lines and b+1 horizontal lines.
# Each rectangle formed on this grid is made up of two vertical lines and two horizontal lines.
# As there are C(a+1,2)=a(a+1)/2 ways of picking two vertical lines and, similarly, b(b+1)/2, ways of picking two horizontal lines.
# Hence, there are a(a+1)b(b+1)/4 rectangles on an a by b rectangular grid.
    
def p85(N = 2*(10**6)):
    x = y = rect_count = 1
    iterations_without_improvement = 0
    best_count = None
    best_pair = (1,1)
    best_diff = N
    tol = int(sqrt(N))
    while iterations_without_improvement < tol:
        if rect_count == N:
            break
        elif rect_count < N:
            x += 1
            y += 1
        else:
            y -= 1
        rect_count = (x*(x+1)*y*(y+1))/4
        if abs(N - rect_count) < best_diff:
            best_diff = abs(N - rect_count)
            best_count = rect_count
            best_pair = x,y
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
    print best_pair, '~~', best_count, '~~', best_diff
    
if __name__ == '__main__':
    t = timeit.Timer('p85()','from __main__ import p85').timeit(1)
    print 'Time:',t