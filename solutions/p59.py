def combinations(values, num):
   for i in xrange(num):
      for v in values:
         

def setup():
   filename = 'C:\\Documents and Settings\\dwaltrip77\\Desktop\\cipher1.txt'
   f = open(filename,'r')
   return [int(c) for c in f.read().split(',')]

def decipher(ciphered_int_list, e_key):
   L = len(ciphered_int_list)
   deciphered = []
   for k in xrange(L):
      for d in xrange(2):
         if k+d < L:
            deciphered.append(chr(ciphered_int_list[k+d] ^ e_key[d]))
   return ''.join(deciphered)

if __name__ == "__main__":
   #import pdb
   #pdb.set_trace()
   ints = setup()
   print decipher(ints, [97,98,99])