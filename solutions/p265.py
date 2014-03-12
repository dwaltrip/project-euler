from collections import defaultdict
import timeit

class SequenceCircle(object):
    def __init__(self, base, N):
        self.base = base
        self.N = N
        self.L = base**N
        self.digits = [str(i) for i in xrange(base)]
        self.partials = defaultdict(list)
        self.partials[N].append('0'*N)
        self.solutions = set()
      
    def build(self):
        for i in xrange(self.N, self.L):
            for partial in self.partials[i]:
                for d in self.digits:
                    new_partial = partial + d
                    if new_partial[-self.N:] not in partial:
                        self.partials[i+1].append(new_partial)
            del self.partials[i]
        for sol in self.partials[self.L]:
            wrap_arounds = set()
            for i in xrange(self.N-1):
                subseq = sol[self.L-(self.N-1-i):] + sol[:i+1]
                if subseq in sol or subseq in wrap_arounds:
                    break
                else:
                    wrap_arounds.add(subseq)
            else:
                self.solutions.add(sol)
            
    def sum(self):
        return sum(int(sol,self.base) for sol in self.solutions)

    def print_solutions(self):
        for sol in self.solutions:
            print sol
        
def main(base, N):
    s1 = 'sc = SequenceCircle(%d, %d)\nsc.build()\nprint sc.sum()' % (base, N)
    s2 = 'from __main__ import SequenceCircle'
    t = timeit.Timer(s1, s2).timeit(1)
    print 'Time:', t
    
if __name__ == '__main__':
    #main(2,5)
    sc = SequenceCircle(2,3)
    sc.build()
    sc.print_solutions()
    print
    sc = SequenceCircle(2,4)
    sc.build()
    sc.print_solutions()
    sc = SequenceCircle(2,6)
    sc.build()
    print '\n' + str(len(sc.solutions))
    