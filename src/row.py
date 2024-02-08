from config import the
import math
import cols
import sys
import l

class ROW:
    def __init__(self, t):
        self.cells = t

    def d2h(self, data):
        d, n, p = 0, 0, 2

        for col in data.cols.y.values():
            x = self.cells[col.at]#.get(col.at)
            if x is None:
                print("?", end="", file=sys.stderr)
            else:
                n += 1
                d += math.pow(abs(col.heaven - col.norm(self.cells[col.at])), p) #removed the .get(col.at)
        
        if n == 0:
            return 0
        else:
            return math.pow(d / n, 1 / p)
        
    def dist(self, other, data):
        d, n, p = 0, 0, the.p
        for col in data.cols.x.values():
            n += 1
            d += col.dist(self.cells[col.at], other.cells[col.at]) ** p
        return math.pow(d / n, 1 / p)
    
    def neighbors(self, data, rows=None):
        if rows is None:
            rows = data.rows
        
        return l.keysort(rows, lambda row: self.dist(row, data))
        
    # def d2h(self, data, d=None, n=None):
    #     d, n = 0, 0
    #     for col in data.cols.y.values():
    #         n += 1
    #         d = d + abs(col.heaven - col.norm(float(self.cells[col.at]))) ** 2
    #     return d ** .5 / n ** .5
    
    # def likes(self, datas, most=None): 
    #     n, nHypotheses = 0, 0
    #     for k, data in datas.items():
    #         n += len(data.rows)
    #         nHypotheses += 1
    #     for k, data in datas.items():
    #         tmp = self.like(data, n, nHypotheses)
    #         if most == None or tmp > most:
    #             most, out = tmp, k
    #     return out
    
    # def like(self, data, n, nHypotheses): 
    #     prior = (len(data.rows) + the.k) / (n + the.k * nHypotheses)
    #     out = math.log(prior)
    #     for col in data.cols.x.values():
    #         v = self.cells[col.at]
    #         if v != '?':
    #             inc  = col.like(v, prior)
    #             if(inc > 0):
    #                 out += math.log(inc)
    #     return math.exp(1) ** out
    
