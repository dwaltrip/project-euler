

black = 1
red = 2
green = 3
blue = 4

def tile_combinations(size, tile_array=[black,red,green,blue]):
    array = [1] + [0]*(size)
    for tile in sorted(tile_array):
        for i in xrange(tile,size+1):
            array[i] += array[i-tile]
    return array
    
def main():
    a = tile_combinations(5, [1,2, 3, 4])
    print a
    
if __name__ == '__main__':
    main()
                
