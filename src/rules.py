import l
from rule import RULE
from config import *

class RULES:
    def __init__(self, ranges, goal, rowss):
        for k, v in enumerate(rowss):
            print(k, len(v))
        
        self.sorted = {}
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0

        self.likeHate()

        for range in ranges.values():
            range.scored = self.score(range.y)

        self.sorted = self.top(self._try(self.top(ranges)))

    def likeHate(self):
        for y, rows in enumerate(self.rowss):
            if y == self.goal:
                self.LIKE += len(rows)
                self.HATE += len(rows)

    def score(self, t):
        return l.score(t, self.goal, self.LIKE, self.HATE)
    
    def _try(self, ranges):
        u = {}
        
        for subset in l.powerset(ranges).values:
            if len(subset) > 0:
                rule = RULE(subset)
                rule.scored = self.score(rule.selectss(self.rowss))
                if rule.scored > 0.01:
                    u.append(rule)
        
        return u
    
    def top(self, t):
        t.sort(key=lambda x: x.scored, reverse=True)
        u = []
        for x in t:
            if x.scored >= t[0].scored * the.Cut:
                u.append(x)
        return l.slice(u, 0, the.Beam)