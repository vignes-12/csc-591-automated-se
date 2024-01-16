import math

class SYM:
    def __init__(self, s="", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0
    
    def add(self, x):
        if x != "?":
            self.n = self.n + 1
            self.has[x] = self.has.get(x, 0) + 1

            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
    
    def mid(self):
        return float(self.mode) if self.mode.isdigit() else 0
    
    def div(self, e):
        e = 0
        for v in self.has.values():
            e = e - v / self.n * math.log(v / self.n, 2)

        return e
    
    def small(self):
        return 0
    
    # TODO - Implement the docstring to use the like function
    # def like(self, x, prior):
    #     return ((self.has[x] or 0) + the.m * prior) / (self.n + the.m)
