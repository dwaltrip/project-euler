from math import sqrt

def minimal_solution(D):
    if sqrt(D) % 1 == 0:
        return 0
    i = 2
    while True:
        if sqrt((i**2 -  1.0) / D) % 1 == 0:
            return i
        i += 1

def main():
    data = []
    highest = 0
    D = 0
    for i in xrange(2,51):
        MS = minimal_solution(i)
        data.append((i,MS))
        if MS > highest:
            D = i
            highest = MS
    print data
    return D
    
if __name__ == '__main__':
    print main()