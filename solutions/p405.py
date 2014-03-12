from __future__ import print_function
               
class grid_point:
    def __init__(self, container_grid, x, y, up=0, right=0, down=0, left=0):
        self.x = x
        self.y = y
        self.up = up
        self.right = right
        self.down = down
        self.left = left
    
class tile_grid:
    def __init__(self, n=0):
        self.n = 0
        self.width = 3
        self.height = 2
        gp = grid_point
        self.grid = [[gp(self, 0, 0, right=1, down=1), gp(self, 1, 0, right=1, left=1), gp(self, 2, 0, left=1, down=1)],
                     [gp(self, 0, 1, right=1, up=1), gp(self, 1, 1, right=1, left=1), gp(self, 2, 1, up=1, left=1)]]
        if n > 0:
            for i in xrange(n):
                self.add_layer()
    
    def add_layer(self):
        z = 1
        
    def pretty_print(self, filepath=None):
        if not filepath:
            action = print
            clean_up = lambda : print("")
            print("")
        else:
            f = open(filepath, "w")
            action = lambda x: f.write(x + "\n")
            clean_up = f.close
            
        action(str("* - " * (self.width - 1) + "*"))
        for y in xrange(1, self.height):
            v_str = [ ]
            h_str = [ ]
            for x in xrange(self.width-1):
                if self.grid[y][x].right:
                    h_str.append("* - ")
                else:
                    h_str.append("*   ")
                if self.grid[y][x].up:
                    v_str.append("|   ")
                else:
                    v_str.append("    ")
            v_str.append("|")
            h_str.append("*")
            
            action(''.join(v_str))
            action(''.join(h_str))
        clean_up()
        
if __name__ == '__main__':
    tg = tile_grid()
    tg.pretty_print(filepath="C:\\Users\\Daniel Waltrip\\Desktop\\fun.txt")

#def draw_tilings(tile_array):
#    print "*-*"
#    print "| |"
#    print "*-*"
#
#draw_tilings([0,1])
#
#def dbl(x):
#    return (x-1)*2 + 1
#
#def double_size(tile_array):
#    height = len(tile_array)
#    width = len(tile_array[0])
#    new_tile_array = [[0 for i in xrange(dbl(width))] for j in xrange(dbl(height))]
#    for y in xrange(len(tile_array)):
#        for x in xrange(len(tile_array[y])):
#            new_tile_array[dbl(y)][dbl(x)] = tile_array[y][x]
#    return new_tile_array
#
#def grow(tile_array, n_plus=1):
#    new_array  = double_size(tile_array)
#    for y in xrange(1, len(new_array)):
#        for x in xrange(1, len(new_array[y])):
#            tl = new_arra[y-1][x-1]
#            bl = new_arra[y+1][x-1]
#            if (tl%4) >= 2 and (tl%8) >= 4 and (bl%2) >= 1 and (bl%4) >= 2:
#                # add in horizontal tiling insert
#                x = x + 4
#            elif (tl%4) >= 2 and (tl%8) >= 4 and (bl%2) >= 1 and (bl%4) >= 2:
#                # add in vertical tiling insert
#                print "hi"
#            else:
#                x = x + 2
#    z = 2
    