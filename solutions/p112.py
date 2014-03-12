import timeit

def is_bouncy(n):
    digits = str(n)
    increasing, decreasing = True, True
    prev = digits[0]
    for i in range(1,len(digits)):
        if digits[i] < prev:
            increasing = False
            break
        prev = digits[i]
    prev = digits[0]
    for i in range(1,len(digits)):
        if prev < digits[i]:
            decreasing = False
            break
        prev = digits[i]
    return (not increasing and not decreasing)

def percent_non_bouncy(target):
	bouncy = 0
	count = 1
	while True:
		bouncy += 1 if is_bouncy(count) else 0
		if (bouncy * 1.0) / count == target:
			return count
		count += 1

if __name__ == '__main__':
    print percent_non_bouncy(.99)
    t = timeit.Timer('percent_non_bouncy(.99)','from __main__ import percent_non_bouncy')
    print 'Time:',t.timeit(1)
