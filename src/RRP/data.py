from row import ROW
from cols import COLS
import csv
import l as lib
import random
from config import *
from node import NODE


class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            with open(src, "r") as input_data:
                csv_reader = csv.reader(input_data)
                for x in csv_reader:
                    self.add(x, fun)

        else:
            if src:
                self.add(src, fun)
            else:
                self.add({}, fun)

    def add(self, t, fun=None, row=None):
        row = t if hasattr(t, 'cells') else ROW(t)

        if self.cols:
            if fun:
                fun(self, row)

            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None):
        u = []

        for _, col in cols.items() if cols else self.cols.all.items():
            u.append(col.mid())

        return ROW(u)

    def div(self, cols=None):
        u = []

        for col in cols.items() if cols else self.cols.all.items():
            u.append(col.div())

        return ROW(u)

    def small(self):
        u = []

        for col in self.cols.all.items():
            u.append(col.small())

        return ROW(u)
    
    def stats(self, cols='y', fun='mid', ndivs=2, u={}):
        u = {".N": len(self.rows)}
        for _, col in self.cols.all.items():
            if cols == 'y' or (cols and col.txt == cols):
                value = getattr(col, fun or "mid", lambda x: x.mid)()
                print(type(value))
                u[col.txt] = lib.rnd(value, ndivs)
                print(u[col.txt])
        filtered_cols = {key: value for key, value in u.items() if key.endswith(
            '!') or key.endswith('+') or key.endswith('-') or key == ".N"}
        return filtered_cols
    
    def clone(self, rows):
        new = DATA(self.cols.names)
        for row in rows or []:
            new.add(row)
        return new
    
    def farapart(self, rows, sortp=None, a=None, b=None, far=None, evals=None):
        far = int(len(rows) * the.Far)
        evals = 1 if a and a.cells is None else 2
        if a is None:
            # Error here!
            a = lib.any(rows).neighbors(self, rows)[far]
        if b is None:
            b = a.neighbors(self, rows)[far]
        if (sortp and b.d2h(self) < a.d2h(self)):
            a, b = b, a
        
        # print("a: ", a)
        # print("b: ", b)
        # print("Dist: ", a.dist(b, self))
        # print("Evals: ", evals)
        return a, b, a.dist(b, self), evals
    
    def half(self, rows, sortp=None, before=None, evals=None):
        some = lib.many(rows, min(the.Half, len(rows)))
        print("Hit in data.half")
        a, b, C, evals = self.farapart(some, sortp, before)
        def d(row1, row2):
            return row1.dist(row2, self)
        def project(r):
            return (d(r, a) ** 2 + C ** 2 - d(r, b) ** 2) / (2 * C)
        as_, bs = [], []
        for n, row in enumerate(lib.keysort(rows, project)):
            if n < len(rows) // 2:
                as_.append(row)
            else:
                bs.append(row)
        return as_, bs, a, b, C, d(a, bs[0]), evals
    
    def tree(self, sortp):
        evals = 0
        def _tree(data, above=None):
            nonlocal evals
            node = NODE(data)
            if len(data.rows) > 2 * (len(self.rows) ** 0.5):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                evals += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)
            return node
        return _tree(self), evals        

    def branch(self, stop=None, rest=None, _branch=None, evals=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))
        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals
            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _= self.half(data.rows, True, above)
                evals += 1
                # rest.extend(rights)
                for row1 in rights.values():
                    rest.append(row1)
                return _branch(data.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals
        return _branch(self)
    
            

    # def gate(self, budget0, budget, some):
    #     stats, bests = [], []

    #     self.rows = l.shuffle(self.rows)
        
    #     top6 = self.rows[:6]
    #     print("1. top6")
    #     for row in top6:
    #         print(row.cells)
    #     print()
        
    #     top50 = self.rows[:50]
    #     print("2. top50")
    #     for row in top50:
    #         print(row.cells)
    #     print()
    #     # Not working past this point

    #     rows_d2h = []
    #     for row in self.rows:
    #         rows_d2h.append((row.d2h(data=DATA("../data/auto93.csv")), row))
    #     rows_d2h = sorted(rows_d2h, key = lambda x: x[0])
    #     print("3. most", rows_d2h[0][1].cells, "\n")

    #     rows = l.shuffle(self.rows)
    #     lite = rows[:budget0+1] #l.slice(rows, 1, budget0)

    #     dark = rows[budget0+1:] #l.slice(rows, budget0+1) # We'll need to adjust the parameter in the function definition of slice()

    #     rows4 = []
    #     rows5 = []
    #     rows6 = []
        
    #     for i in range(budget): #Using +1 to include all values in budget
    #         lite_d2h = []
    #         for row in lite:
    #             lite_d2h.append((row.d2h(data=DATA("../data/auto93.csv")), row))
    #         lite_d2h = sorted(lite_d2h, key = lambda x: x[0])
    #         best, rest = self.bestRest(lite, len(lite) ** some)
    #         todo, selected = self.split(best, rest, lite, dark)
    #         stats.append(selected.mid())
    #         bests.append(best.rows[0]) #Lua lists are indexed starting at 1, python is 0
    #         # print("4: rand")
    #         rand_rows = random.sample(dark, budget0)
    #         for row in rand_rows:
    #             # print(row.cells)
    #             rows4.append(row)
                

    #         # print("5: mid\n", selected.mid().cells)
    #         rows5.append(selected.mid())

    #         # print("6: top\n", bests[-1].cells)
    #         rows6.append(bests[-1])
    #         lite.append(dark.pop(todo))
        
    #     print("4: rand")
    #     for row in rows4:
    #         print(row.cells)
    #     print()
        
    #     print("5: mid")
    #     for row in rows5:
    #         print(row.cells)
    #     print()

    #     print("6: top")
    #     for row in rows6:
    #         print(row.cells)
    #     print()
        
    #     return stats, bests
    

    # def split(self, best, rest, lite, dark):
    #     selected = DATA(self.cols.names)
    #     max = 1E30
    #     out = 1

    #     for i, row in enumerate(dark):
    #         b = row.like(best, len(lite), 2)
    #         r = row.like(rest, len(lite), 2)
            
    #         if b > r:
    #             selected.add(row)
            
    #         tmp = abs(b + r) / abs(b - r + 1E-300)

    #         if tmp > max:
    #             out, max = i, tmp

    #     return out, selected

    # def bestRest(self, rows, want, best=None, rest=None, top=None):
    #     rows.sort(key = lambda row: row.d2h(self))

    #     best, rest = DATA(self.cols.names), DATA(self.cols.names)

    #     for i, row in enumerate(rows):
    #         if i <= want:
    #             best.add(row)
    #         else:
    #             rest.add(row)
        
    #     # print("Best: ", len(best))
    #     # print("Rest: ", len(rest))
    #     return best, rest
