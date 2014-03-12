from math import sqrt

def blue_discs(n):
   return int(sqrt((n-1)*n/2.0 + .25)+.5)

nlist = []
blist = []
for n in xrange(10,1000000):
   b = blue_discs(n)
   if n*(n-1.0)/(b*(b-1.0))==2:
      nlist.append(n)
      blist.append(b)
      print n,'~~',b
      
print '\n** ratios between successive n-values**'
for i in xrange(1,len(nlist)):
   print '%d / %d =\n\t' %(nlist[i],nlist[i-1]),(nlist[i]*1.0)/nlist[i-1]

print '\n** ratios between successive b-values**'
for i in xrange(1,len(blist)):
   print '%d / %d =\n\t' %(blist[i],blist[i-1]),(blist[i]*1.0)/blist[i-1]
   
print '\n** ratios between n-values and b-values**'
for i in xrange(len(blist)):
   print '%d / %d =\n\t' %(blist[i],nlist[i]),(blist[i]*1.0)/nlist[i]