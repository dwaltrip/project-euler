from timeit import Timer

class Cell(object):
    def __init__(self, x_y, ways):
        self.x, self.y = x_y
        self.ways = ways
        self.roll_dict = {}

def get_roll_dict(n, upper, m):
    """
    Calculates all the different possible rolls of 'n' dice, ignoring order,
    if 'upper' is the highest allowed roll for a single die.
    This function assumes 'upper' is less than or equal to the number of sides on the dice.
    """
    roll_dict = {}
    max_total = n * upper
    array = calc_ways(n, m, n, max_total)
    for row in array:
        for cell in row:
            for roll,data in cell.roll_dict.items:
                if roll in roll_dict:
                    roll_dict[roll] += data.ways
                else:
                    roll_dict[roll] = data.ways
    return roll_dict


def calc_ways(n, m, a, total, print_array=False):
    """
    Calculates the number of ways to roll 'n' dice with 'm' sides
    such that the top 'a' dice add up to 'total'.
    """
    # array = [[1]*m + [0]*(total-m)]
    # for i in range(a):
        # array.append([0 for j in range(total)])
    array = []
    for i in xrange(a):
        array.append([Cell((j,i),0) for j in xrange(total)])
    for j in xrange(m):
        roll = (0,)*(j) + (1,) + (0,)*(m-j-1)
        array[0][j].ways = 1
        array[0][j].roll_dict = {roll:1}

    for j in xrange(1,total):
        for i in xrange(1,a):
            if i == j:
                # array[i][j] = 1
                array[i][j].ways = 1
                roll = (i+1,) + (0,)*(m-1) 
                array[i][j].roll_dict = {roll:1}
            elif i < j:
                lower = j - m if j - m > 0 else 0
                foo = array[i-1][lower:j]
                ways_sum = 0
                for cell in foo:
                    ways_sum += cell.ways
                    for roll,ways in cell.roll_dict.iteritems():
                        new_roll = list(roll)
                        new_roll[j - cell.x - 1] += 1
                        new_roll = tuple(new_roll)
                        if new_roll in array[i][j].roll_dict:
                            array[i][j].roll_dict[new_roll] += ways
                        else:
                            array[i][j].roll_dict[new_roll] = ways
                array[i][j].ways = ways_sum

    # b = n - a
    # roll_dict = array[a-1][total-1].roll_dict
    # if b == 0:
        # pass
    # else:
        # for roll,data in roll_dict.keys():
            # lowest = None
            # for i in range(len(roll)):
                # if roll[i] != 0:
                    # lowest = i + 1
                    # break
            # if not Lowest:
                # print '~~~~ Houston we have a problem! ~~~~~'
                # assert False
            # else:
                # data.roll_dict_b = get_roll_dict(b, lowest, m)


    #if print_array:
    #    for row in array:
    #        for cell in row:
    #            #print cell.roll_dict.keys() if cell.roll_dict.keys() else [[0]*m],
    #            print cell.ways,
    #        print
    #return array

    import csv
    with open("c:\\users\\DanielW\\desktop\\p240_example.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows([[cell.ways for cell in row] for row in array])

    print
    print 'done writing'
    print

if __name__ == '__main__':
    calc_ways(5,6,3,15, print_array=True)
    #calc_ways(20,12,10,70, print_array=True)
    # print calc_ways(20,12,10,70).ways
    # # t = Timer('calc_ways(5,6,15)','from __main__ import calc_ways')
    # # print 'Time elapsed:', t.timeit(1)
