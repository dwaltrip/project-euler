from timeit import Timer
from math import factorial

def permutations(roll):
    roll = list(roll)
    numerator = factorial(sum(roll))
    denom = 1
    for d in roll:
        denom *= factorial(d)
    try:
        p = numerator / denom
    except (Exception):
        print 'ERROR ~~~~~ roll:',roll,'-- numerator:',numerator,'-- denom:',denom
        raise Exception
    return p
    
class Cell(object):
    def __init__(self, x_y):
        self.x, self.y = x_y
        self.roll_set = set()
        
def array_builder(n, m, total):
    array = []
    for i in range(n):
        array.append([Cell((j,i)) for j in range(total)])
    for j in range(m if m < total else total):
        roll = (0,)*(j) + (1,) + (0,)*(m-j-1)
        array[0][j].roll_set.add(roll)
    
    for j in range(1,total):
        for i in range(1,n):
            if i == j:
                roll = (i+1,) + (0,)*(m-1) 
                array[i][j].roll_set.add(roll)
            elif i < j:
                lower = j - m if j - m > 0 else 0
                foo = array[i-1][lower:j]
                for cell in foo:
                    for roll in cell.roll_set:
                        new_roll = list(roll)
                        new_roll[j - cell.x - 1] += 1
                        new_roll = tuple(new_roll)
                        array[i][j].roll_set.add(new_roll)
    return array
        
def combine(r1, r2):
    assert len(r1) == len(r2)
    combo = [0]*len(r1)
    for i in range(len(r1)):
        combo[i] += r1[i] + r2[i]
    combo = tuple(combo)
    return combo
        
def add_lower_dice(roll, n, m):
    """
    Calculates all the different possible rolls of 'n' dice, ignoring order,
    if 'upper' is the highest allowed roll for a single die.
    This function assumes 'upper' is less than or equal to the number of sides on the dice.
    """
    no_zeros_roll = []
    for i in roll:
        if i != 0: no_zeros_roll.append(i)
    if not no_zeros_roll:
        print '~~~~ Houston we have a problem! ~~~~~'
        assert False
    else:
        dice_max = roll.index(min(no_zeros_roll)) + 1
    roll_set = set()
    max_total = n * dice_max
    array = array_builder(n, m, max_total)
    tester = (0,)*(m - dice_max)
    for cell in array[len(array)-1]:
        for lower_dice in cell.roll_set:
            if lower_dice[dice_max:] == tester and lower_dice.roll_set != (0,)*m:
                roll_set.add(combine(roll,lower_dice))
    return roll_set
    
def get_lower_dice(roll, n, m):
    """
    Calculates all the different possible rolls of 'n' dice, ignoring order,
    if 'upper' is the highest allowed roll for a single die.
    This function assumes 'upper' is less than or equal to the number of sides on the dice.
    """
    no_zeros_roll = []
    for i in roll:
        if i != 0: no_zeros_roll.append(i)
    if not no_zeros_roll:
        print '~~~~ Houston we have a problem! ~~~~~'
        assert False
    else:
        dice_max = roll.index(min(no_zeros_roll)) + 1
    lower_dice_roll_set = set()
    max_total = n * dice_max
    array = array_builder(n, m, max_total)
    tester = (0,)*(m - dice_max)
    for cell in array[len(array)-1]:
        for lower_roll in cell.roll_set:
            if lower_roll[dice_max:] == tester:
                lower_dice_roll_set.add(lower_roll)
    return lower_dice_roll_set

            
        
def calc_ways(n, m, a, total):
    """
    Calculates the number of ways to roll 'n' dice with 'm' sides
    such that the top 'a' dice add up to 'total'.
    """    
    # array = [[1]*m + [0]*(total-m)]
    # for i in range(a):
        # array.append([0 for j in range(total)])
    print '~~~ STARTING PART ONE ~~~'
    array = array_builder(a, m, total)

    b = n - a
    upper_dice_roll_set = array[a-1][total-1].roll_set
    complete_roll_set = set()
    if b > 0:
        print '~~~ STARTING PART TWO ~~~'
        print 'b:',b,'--- m:',m,'--- len(upper_dice_roll_set) =',len(upper_dice_roll_set)
        tick = 91
        for i,roll in enumerate(upper_dice_roll_set):
            if (i+1) % tick == 0:
                print str((i+1)/tick) + '% complete!'
            lower_dice_roll_set = get_lower_dice(roll, b, m)
            complete_roll_set.update(lower_dice_roll_set)
            # for lower_roll in lower_dice_roll_set:
                # complete_roll_set.add(combine(roll,lower_roll))
                
    # p = 0
    # for roll in complete_roll_set:
        # p += permutations(roll)
    
    # f = open('c:\\pythonwork\\project_euler\\p240_answer.txt','wb')
    # f.write(p)
    # f.close()
    # return p
    return array, upper_dice_roll_set, complete_roll_set
    
def print_array(array):
    for row in array:
        for cell in row:
            p = 0
            for roll in cell.roll_set:
                p += permutations(roll)
            spaces = 8 - len(str(p))
            print str(p) + spaces*' ',
        print

# if __name__ == '__main__':
   # print calc_ways(20,12,10,70)
   # # t = Timer('calc_ways(5,6,15)','from __main__ import calc_ways')
   # # print 'Time elapsed:', t.timeit(1)
   
### QUICK ACCESS ####
# >>> import sys
# >>> sys.path.append('c:\pythonwork\project_euler')
# >>> from problem_240b import calc_ways, permutations, print_array
# >>> a,crd = calc_ways(5,6,3,15)