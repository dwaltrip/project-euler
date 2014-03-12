from math import ceil,sqrt

def special_2_sqr_sums_up_to(n):
    loop_limit = int(ceil(sqrt(n / 2)))
    print 'limit:',loop_limit
    d = {}
    for i in range(1,loop_limit+1):
        for j in range(1,i+1):
            new = [(a*i**2 + b*j**2, (i,j),b) for a,b in [(1,1), (1,2), (1,3), (1,7)]]
            new.extend([(a*i**2 + b*j**2,(j,i),a) for a,b in [(2,1), (3,1), (7,1)]])
            for num, s1_s2, c in new:
                if num not in d:
                    d[num] = {1:None, 2:None, 3:None, 7:None}
                d[num][c] = s1_s2
        if i % (loop_limit**2 /400) == 0:
            print str(i / (loop_limit**2 /400)) + '% complete!'
    return d

if __name__ == '__main__':
    limit = 10000000
    d = special_2_sqr_sums_up_to(limit)
    nums = d.items()
    nums.sort()
    goods = []
    highest = 0
    for n in nums:
        if n[0] > limit:
            continue
        if n[1][1] and n[1][2] and n[1][3] and n[1][7]:
            goods.append(n)
            if n[0] > highest:
                highest = n[0]
    print 'highest:', highest
    print 'number of results:',len(goods)