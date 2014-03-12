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
    
class MinimalSumPathFinder(object):
    def __init__(self,matrix):
        self.matrix = matrix
        self.h, self.w = len(matrix), len(matrix[0])
        
    def node_value(self, coord):
            return self.matrix[coord[0]][coord[1]]
            
    def compute_path(self, start, goal):
        msp_matrix = [[-1 for i in xrange(self.w)] for j in xrange(self.h)]
        msp_matrix[start[0]][start[1]] = self.node_value(start)
        
        def move_cost(coord):
            return msp_matrix[coord[0]][coord[1]]
        
        open_set = []
        closed_set = {}
        paths = defaultdict(list)
        paths[start].append(start)
        
        start_node = [start,move_cost(start)]
        open_set.append(start_node)
        curr_node = start_node
        
        while open_set:
            curr_node = open_set.pop(0)
            if curr_node[0] == goal:
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
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= cx+dx < self.w and 0 <= cy+dy < self.h:
                slist.append((cy+dy,cx+dx))
        return slist
        
    def path_sum(self, path):
        return sum((self.node_value(coord) for coord in path))
    
def p83():
    lines = open('c:\\pythonwork\\project_euler\\matrix.txt').readlines()
    matrix = [[int(s) for s in line.split(',')] for line in lines]
    mspf = MinimalSumPathFinder(matrix)
    path = mspf.compute_path((0,0),(79,79))
    print mspf.path_sum(path)
    
def p83b():
    lines = open('c:\\pythonwork\\project_euler\\matrix.txt').readlines()
    matrix = [[int(s) for s in line.split(',')] for line in lines]
    ncols, nrows = len(matrix), len(matrix[0])
    min_sums = [[0 for i in xrange(ncols)] for j in xrange(nrows)]
    min_sums[0][0] = matrix[0][0]
    
    
    
if __name__ == '__main__':
    t = timeit.Timer('p83()','from __main__ import p83').timeit(1)
    print 'Time:', t