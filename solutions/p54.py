import operator
import timeit
import cProfile

RANKS = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}
    
HAND_RANK = {
    'high card':1,
    'one pair':2,
    'two pair':3,
    'three of a kind':4,
    'straight':5,
    'flush':6,
    'flush':7,
    'full house':8,
    'four of a kind':9,
    'straight flush':10
}

class Card(object):
    def __init__(self, rank, suit):
        self.rank = RANKS[rank]
        self.suit = suit

class Hand(object):
    def __init__(self,cards):
        self.cards = sorted([Card(c[0], c[1]) for c in cards], key=operator.attrgetter('rank'), reverse=True)
        self.set_hand_rank()
        
    def set_attr(self):
        straight, flush = True, True
        for i, card in enumerate(self.cards):
            if i == 4: break
            next_card = self.cards[i+1]
            if card.suit != next_card.suit:
                flush = False
            if card.rank - 1 != next_card.rank:
                straight = False
        self.flush, self.straight = flush, straight
        groups = set(c.rank for c in self.cards)
        groups = sorted([(len([c for c in self.cards if c.rank == r]),r) for r in groups], key=operator.itemgetter(1), reverse=True)
        groups.sort(key=operator.itemgetter(0), reverse=True)
        self.groups = groups
        
    def set_hand_rank(self):
        self.set_attr()
        if self.flush and self.straight:
            self.rank = 'straight flush'
        elif self.groups[0][0] == 4:
            self.rank = 'four of a kind'
        elif self.groups[0][0] == 3 and self.groups[1][0] == 2:
            self.rank = 'full house'
        elif self.flush:
            self.rank = 'flush'
        elif self.straight:
            self.rank = 'straight'
        elif self.groups[0][0] == 3:
            self.rank = 'three of a kind'
        elif self.groups[0][0] == 2 and self.groups[1][0] == 2:
            self.rank = 'two pair'
        elif self.groups[0][0] == 2:
            self.rank = 'one pair'
        else:
            self.rank = 'high card'
            
    def get_hand_rank(self):
        return HAND_RANK[self.rank]
    hand_rank = property(get_hand_rank)
    
    def is_better_than(self, other_hand):
        if self.hand_rank > other_hand.hand_rank:
            return True
        elif self.hand_rank < other_hand.hand_rank:
            return False
        else:
            i = 0
            while self.groups[i][1] == other_hand.groups[i][1]:
                i += 1
            return self.groups[i][1] > other_hand.groups[i][1]
        
def main():
    f = open('c:\pythonwork\project_euler\poker.txt','r')
    p1_wins = 0
    for line in f.readlines():
        cards = line.split(' ')
        h1 = Hand(cards[:5])
        h2 = Hand(cards[5:])
        if h1.is_better_than(h2):
            p1_wins += 1
    return p1_wins
    
if __name__ == '__main__':
    print main()
    t = timeit.Timer('main()', 'from __main__ import main')
    print 'Time:', t.timeit(1)
    cProfile.run('main()')