import timeit

DIVISORS = {2:2, 3:3, 4:5, 5:7, 6:11, 7:13, 8:17}
def test_sub_str_div(s):
    for i in xrange(2,9):
        if int(s[i-1:i+2]) %  DIVISORS[i] != 0:
            return False
    return True

def gen_perms(chars):
	if len(chars)<=1:
		yield chars
	else:
		for p in gen_perms(chars[1:]):
			for i in xrange(len(p)+1):
				yield p[:i] + chars[0] + p[i:]
    
def gen_char_and_rest(chars):
    for i in xrange(len(chars)):
        yield (chars[i], chars[:i] + chars[i+1:])
    
def main():
    total = 0
    for e,rest in gen_char_and_rest('02468'):
        for sub_str in gen_perms('1379'+rest):
            s = sub_str[:3] + e + sub_str[3] + '5' + sub_str[4:]
            if test_sub_str_div(s):
                total += int(s)
    return total
    
if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main')
    print 'Time:', t.timeit(1)