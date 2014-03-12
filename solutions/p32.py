digits = set('123456789')
pandigitals = []
for i1 in xrange(1, 4876):
    if len(str(i1)) == 3: i2_limit = 99
    elif len(str(i1)) == 4: i2_limit = 9
    else: i2_limit = i1
    for i2 in xrange(1, i2_limit):
        s1,s2,s3 = str(i1),str(i2),str(i1*i2)
        if '0' not in s1+s2+s3 and len(str(s1+s2+s3)) == 9 and set(s1+s2+s3) == digits and int(s3) not in pandigitals:
            pandigitals.append(int(s3))
        if i1*i2 > 9999:
            break
print 'The sum of all pan-digital:', sum(pandigitals)
