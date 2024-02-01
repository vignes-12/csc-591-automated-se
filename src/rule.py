from misc import _showLess

class RULE:
    def __init__(self, ranges):
        self.parts = {}
        self.scored = 0
        for range in ranges.values():
            t = self.parts.get(range.txt, [])
            t.append(range)
            self.parts[range.txt] = t

    def _or(self, ranges, row, x=None, lo=None, hi=None):
        x = row.cells[ranges[1].at]
        if x == "?":
            return True
        for range in ranges.values():
            lo, hi = range.x['lo'], range.x['hi']
            if (lo == hi and lo == x) or (lo <= x and x < hi):
                return True
        return False
    
    def _and(self, row):
        for ranges in self.parts.values():
            if not self._or(ranges, row):
                return False
        return True
    
    def selects(self, rows):
        t = []
        for r in rows:
            if self._and(r):
                t.append(r)
        return t
    
    def selectss(self, rowss, t):
        t = {}
        for y, rows in enumerate(rowss):
            t[y] = len(self.selects(rows))
        return t
    
    def show(self, ands=None):
        ands = []
        for ranges in self.parts.values():
            ors = _showLess(ranges)
            at = None
            for i, range in enumerate(ors):
                at = range.at
                ors[i] = range.show()
            ands.append(" or ".join(ors))
        return " and ".join(ands)
    