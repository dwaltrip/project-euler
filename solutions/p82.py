from collections import defaultdict
import timeit

def binary_insert(lst, item, f):
    a,b = 0, len(lst)-1
    m = (a+b)/2
    if lst:
        while lst[m] != item and a<=b:
            if f(lst[m]) < f(item):
                a = m + 1
            else:
                b = m - 1
            m = (a+b)/2
    lst.insert(m+1,item)
    
class MultiPathFinder(object):
    def __init__(self,matrix):
        self.matrix = matrix
        self.h, self.w = len(matrix), len(matrix[0])
        
    def node_value(self, coord):
        return self.matrix[coord[0]][coord[1]]
            
    def compute_path(self, start_points, goal_points):
        msp_matrix = [[-1 for i in xrange(self.w)] for j in xrange(self.h)]
        
        def move_cost(coord):
            return msp_matrix[coord[0]][coord[1]]
        
        open_set = []
        closed_set = {}
        paths = defaultdict(list)
        
        for start in start_points:
            msp_matrix[start[0]][start[1]] = self.node_value(start)
            paths[start].append(start)
            binary_insert(open_set,[start,move_cost(start)], lambda x: x[1])
        
        while open_set:
            curr_node = open_set.pop(0)
            if curr_node[0] in goal_points:
                return paths[curr_node[0]]
                
            closed_set[curr_node[0]] = curr_node[0]
            for next in self.successors(curr_node[0]):
                if next in closed_set:
                    continue
                new_cost = move_cost(curr_node[0]) + self.node_value(next)
                if move_cost(next) < 0:
                    binary_insert(open_set,[next,new_cost],lambda x: x[1])
                    paths[next].extend(paths[curr_node[0]] + [next])
                    msp_matrix[next[0]][next[1]] = new_cost
                elif new_cost < move_cost(next):
                    paths[next] = paths[curr_node[0]] + [next]
                    msp_matrix[next[0]][next[1]] = new_cost
                    k = -1
                    for i,node in enumerate(open_set):
                        if node[0] == next:
                            k = i
                            break
                    if k != -1:
                        del open_set[k]
                        binary_insert(open_set,[next,new_cost],lambda x: x[1])
        return []
    
    def successors(self, coord):
        cy,cx = coord
        slist = []
        for dy,dx in [(1,0),(0,1),(-1,0)]:
            if 0 <= cx+dx < self.w and 0 <= cy+dy < self.h:
                slist.append((cy+dy,cx+dx))
        return slist
        
    def path_sum(self, path):
        return sum((self.node_value(coord) for coord in path))
    
def p82():
    lines = open('C:\\Users\\Daniel Waltrip\\Desktop\\daniel stuff 30-7-2011\\pythonwork\\project_euler\\matrix.txt').readlines()
    matrix = [[int(s) for s in line.split(',')] for line in lines]
    mpf = MultiPathFinder(matrix)
    start_points = [(i,0) for i in xrange(80)]
    end_points = [(i,79) for i in xrange(80)]
    path = mpf.compute_path(start_points,end_points)
    print mpf.path_sum(path)    
    
if __name__ == '__main__':
    t = timeit.Timer('p82()','from __main__ import p82').timeit(1)
    print 'Time:', t