# solves project euler problem 205
import timeit
import cProfile

def ways_to_roll_array(n, m):
    """
    Creates an 2d-array that you can access like so: a[i][j] = the number of ways to roll (i + 1) dice with 'm' sides each so that they add to the total of (j + 1),
    where 0 <= i <= n - 1 and 0 <= j <= (n * m) - 1.
    """
    total = n*m
    array = [[1]*m + [0]*(total-m)]
    for i in xrange(1, n):
        array.append([0 for j in xrange(total)])
    for i in xrange(1,n):
        ways = 0
        prev_row = array[i-1]
        curr_row = array[i]
        for j in xrange(1, total):
            if i == j:
                curr_row[j] = 1
            elif i < j:
                lower = j - m if j - m > 0 else 0
                if not ways:
                    for k in xrange(lower, j):
                        ways += prev_row[k]
                else:
                    ways += (-prev_row[lower-1] + prev_row[j-1]) if lower else prev_row[j-1]
                curr_row[j] = ways
    return array

from decimal import Decimal as D
def dice_prob(n1, s1, n2, s2):
    a1 = ways_to_roll_array(n1, s1)
    a2 = ways_to_roll_array(n2, s2)
    p1_max, p2_max = n1*s1, n2*s2
    p1_wins = 0
    p2_ways_sum = sum(a2[n2-1][i] for i in xrange(0,n1-2))
    for current_tot in xrange(n1, p1_max + 1):
        if current_tot > p2_max:
            break
        if current_tot <= n2:
            continue
        p1_ways_current = a1[n1-1][current_tot-1]
        p2_ways_sum += a2[n2-1][current_tot-2]
        p1_wins += p1_ways_current * p2_ways_sum 
    return p1_wins / (D(s1**n1) * D(s2**n2))
    
if __name__ == '__main__':
    n1, s1, n2, s2 = 9, 4, 6, 6
    print dice_prob(n1,s1,n2,s2)
    t = timeit.Timer('dice_prob(n1, s1, n2, s2)', 'from __main__ import dice_prob, n1, s1, n2, s2').timeit(1)
    print 'Time:', t
    cProfile.run('dice_prob(n1, s1, n2, s2)')