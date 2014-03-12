import timeit
import cProfile

letter_values = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
    'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
    'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
word_values = {}

def main():
    f = open('c:\pythonwork\project_euler\words.txt','r')
    data = f.read()
    f.close()
    words = data.split('","')
    words[0] = words[0].strip('"')
    words[len(words)-1] =  words[len(words)-1].strip('"')
    for word in words:
        s = 0
        for letter in word:
            s += letter_values[letter]
        if s in word_values:
            word_values[s] += 1
        else:
            word_values[s] = 1
    limit = max(word_values.keys())
    triangle_nums = set()
    n = triangle = 1
    while triangle < limit:
        triangle = (n*(n+1))/2
        triangle_nums.add(triangle)
        n += 1
    total = 0
    for value,count in word_values.iteritems():
        if value in triangle_nums:
            total += count
    return total

if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()','from __main__ import main')
    print 'Time:', t.timeit(1)
    cProfile.run('main()')