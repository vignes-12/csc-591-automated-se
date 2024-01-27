from row import ROW
from cols import COLS
import csv
import l
import math


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
            # for x in src if src else {}:
            #     print("X: ", x)
            #     self.add(x, fun)
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

    def mid(self, cols, u):
        u = {}

        for col in cols.items() if cols else self.cols.all.items():
            u.append(col.mid())

        return ROW(u)

    def div(self, cols, u):
        u = {}

        for col in cols.items() if cols else self.cols.all.items():
            u.append(col.div())

        return ROW(u)

    def small(self, u):
        u = {}

        for col in self.cols.all.items():
            u.append(col.small())

        return ROW(u)
    
    def stats(self, cols='y', fun='mid', ndivs=2, u={}):
        u = {".N": len(self.rows)}
        for _, col in self.cols.all.items():
            if cols == 'y' or (cols and col.txt == cols):
                value = getattr(col, fun or "mid", lambda x: x.mid)()
                u[col.txt] = l.rnd(value, ndivs)
        filtered_cols = {key: value for key, value in u.items() if key.endswith(
            '!') or key.endswith('+') or key.endswith('-') or key == ".N"}
        return filtered_cols

    def gate(self, budget0, budget, some):
        stats, bests = {}, {}

        self.rows = l.shuffle(self.rows)
        
        top6 = self.rows[:6]
        print("1. top6")
        for row in top6:
            print(row.cells)

        top50 = self.rows[:50]
        print("2. top50")
        for row in top50:
            print(row.cells)

        # Not working past this point

        rows_d2h = []
        for row in self.rows:
            rows_d2h.append(row.d2h(data=DATA("../data/diabetes.csv")))
        rows_d2h.sort()
        print("3. most", rows_d2h[0])

        rows = l.shuffle(self.rows)
        lite = l.slice(rows, 1, budget0)
        dark = l.slice(rows, budget0+1) # We'll need to adjust the parameter in the function definition of slice()

        for i in range(budget): #Using +1 to include all values in budget
            lite_d2h = []
            for row in lite:
                lite_d2h.append(row.d2h(data=DATA("../data/diabetes.csv")))
            lite_d2h.sort()
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            stats.append(selected.mid())
            bests.append(best.rows[0]) #Lua lists are indexed starting at 1, python is 0
            print("4: rand", self.cols.y[l.rnd(0, len(dark))])
            print("5: mid", selected.mid().y)
            print("6: top", bests[-1].y)
            lite.append(dark.pop(todo))
        
        return stats, bests

    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names)
        max = 1E30
        out = 1

        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            
            if b > r:
                selected.add(row)
            
            tmp = abs(b + r) / abs(b - r + 1E-300)

            if tmp > max:
                out, max = i, tmp

        return out, selected

    def bestRest(self, rows, want, best, rest, top=None):
        rows.sort(key = lambda row: row.d2h(self))

        best, rest = self.cols.names

        for i, row in enumerate(rows):
            if i <= want:
                best.append(row)
            else:
                rest.append(row)
        return DATA(best), DATA(rest)
