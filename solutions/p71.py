from itertools import izip_longest, izip, chain
import math
import timeit

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def gen_branch(starting_xy, branching_functions, n=10, max_ratio=None):
    branch = [starting_xy]
    exp = len(branching_functions)
    level = 0
    start_pos = 0
    end_pos = 1
    while(level < n):
        branch.extend(f(x,y) for f in branching_functions for x,y in branch[start_pos:end_pos])
        level = level + 1
        start_pos = start_pos + exp**(level - 1)
        end_pos = end_pos + exp**(level)
    return branch

def gen_branch_dict(starting_xy, branching_functions, n=10):
    branch = {0: [starting_xy]}
    exp = len(branching_functions)
    level = 0
    start_pos = 0
    end_pos = 1
    while(level < n):
        level = level + 1
        branch[level] = [f(x,y) for f in branching_functions for x,y in branch[level-1]]
        start_pos = start_pos + exp**(level - 1)
        end_pos = end_pos + exp**(level)
    return branch
    
def p71(upper_bound=(3,7), max_denom=10**6):
    upper_n, upper_d = upper_bound
    upper_n = upper_n * 1.0
    
    current_best_ratio = 2.0 / 5
    count = 0
    for i in xrange(8, max_denom):
        next_try = int(math.floor((upper_n * i) / upper_d))
        while gcd(i, next_try) > 1:
            next_try = next_try - 1
        if ((next_try * 1.0) / i) > current_best_ratio:
            curret_best_ratio = ((next_try * 1.0) / i)
            current_best_pair = (next_try, i)
        count = count + (int(math.floor((upper_n * i) / upper_d)) - next_try)
    print "inner_loop_counts:", count
    print "winner:", current_best_pair
    
    return current_best_pair
    
if __name__ == '__main__':
    t = timeit.Timer('p71()','from __main__ import p71,gcd').timeit(1)
    print 'Time:', t
    
    ### everything below this was misguided attempts to solve the problem by generating coprime lists
    ### this is foolish as ~60% of all pairs of numbers are coprimes, we need to look much more narrowly
    ### so for each n: 1 to max_n, we find the biggest number m such m < floor(3*n/7) and gcd(floor(3*n/7),m) == 1
    ### we take the max of these, with ratio size as comparison function, and that is answer
    
    #branching_functions = [(lambda m, n: (2*m - n, m)), (lambda m, n: (2*m + n, m)), (lambda m, n: (m + 2*n, n))]
    #
    #print gen_branch((2, 1), branching_functions, n=3)
    #
    #for val1, val2 in izip_longest(sorted(gen_branch((2, 1), branching_functions, n=3), key= lambda x_y: x_y[0]),
    #                               sorted(gen_branch((2, 1), branching_functions, n=4), key= lambda x_y: x_y[0])):
    #    print val1, "~~", val2
    
    #lower_d, lower_n = lower_bound
    #lower_n = lower_n * 1.0
    
    #coprimes = gen_branch((2, 1), branching_functions, n=15)
    #coprimes.extend(gen_branch((3,1), branching_functions, n=15))
    #coprimes.sort(key= lambda x_y: (1.0*x_y[1]/x_y[0]))
    #for i,x_y in enumerate(coprimes):
    #    if x_y == (7,3):
    #        print coprimes[i-1]
    #print max(coprimes, key= lambda x_y: x_y[0])
    
    #branch_dict = gen_branch_dict((2, 1), branching_functions, n=5)
    #val_lists_by_denom = []
    #val_lists_by_ratio = []
    #for k in sorted(branch_dict.keys()):
    #    val_lists_by_denom.append(sorted(branch_dict[k], key= lambda x_y: x_y[0]))
    #    val_lists_by_ratio.append(sorted(branch_dict[k], key= lambda x_y: ((x_y[1]*1.0)/x_y[0])))
    
    #def output_max_x_min_x(x=5, lists=[], filename=''):
    #    max_val = len(str(max(chain(*lists), key=lambda x: len(str(x))))) + 5
    #    n = len(lists)
    #    def fmt_fn(vals, new_line=True):
    #        prefix = '\n' if new_line else ''
    #        return prefix + ' '.join(str(v).ljust(max_val) for v in vals)
    #    
    #    min_rows, max_rows = [], []
    #    for i in xrange(x): 
    #        min_rows.append([lst[i] if i < len(lst) else '-' for lst in lists])
    #        max_rows.append([lst[-(i+1)] if i < len(lst) else '-' for lst in lists])
    #    
    #    lines = chain([['Max Values']], max_rows, [['\nMin Values']], min_rows)
    #    if filename:
    #        with open("C:\\Users\\Daniel Waltrip\\Desktop\python\\" + filename, 'w+') as f:
    #            for i,text_line in enumerate(lines):
    #                f.write(fmt_fn(text_line, new_line=(i>0)))
    #    else:
    #        for text_line in lines:
    #            print text_line
    #
    #output_max_x_min_x(x=10, lists=val_lists_by_denom, filename="by_denom.txt")
    #output_max_x_min_x(x=10, lists=val_lists_by_ratio, filename="by_ratio.txt")
    
        