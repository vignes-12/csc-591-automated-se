from row import ROW
from cols import COLS
import csv
import l


class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            with open(src, "r") as input_data:
                # print("Beginning of Input Read")
                csv_reader = csv.reader(input_data)
                # print("Whole file: ", csv_reader)
                for x in csv_reader:
                    # print("X within isInstance: ", x)
                    self.add(x, fun)

        else:
            # print("SRC: ", src)
            # for x in src if src else {}:
            #     print("X: ", x)
            #     self.add(x, fun)
            if src:
                self.add(src, fun)
            else:
                self.add({}, fun)

    def add(self, t, fun=None, row=None):
        # print("T: ", t)
        row = t if hasattr(t, 'cells') else ROW(t)
        # print("Row: ", row.cells)

        if self.cols:
            # print("Hit in self.cols block")
            if fun:
                # print("Hit in fun: ", fun)
                fun(self, row)

            self.rows.append(self.cols.add(row))
        else:
            # print("Hit in Data: COLS(row)")
            self.cols = COLS(row)

    def mid(self, cols, u):
        u = {}

        for col in cols.items() if cols else self.cols.all.items():
            # print("hit in mid")
            u.append(col.mid())

        return ROW(u)

    def div(self, cols, u):
        u = {}

        for col in cols.items() if cols else self.cols.all.items():
            # print("hit in div")
            u.append(col.div())

        return ROW(u)

    # def small(self, u):
    #     u = {}

    #     for col in self.cols.all.items():
    #         u.append(col.small())

    #     return ROW(u)
    def stats(self, cols='y', fun='mid', ndivs=2, u={}):
        u = {".N": len(self.rows)}
        for _, col in self.cols.all.items():
            if cols == 'y' or (cols and col.txt == cols):
                value = getattr(col, fun or "mid", lambda x: x.mid)()
                u[col.txt] = l.rnd(value, ndivs)
        filtered_cols = {key: value for key, value in u.items() if key.endswith(
            '!') or key.endswith('+') or key.endswith('-') or key == ".N"}
        return filtered_cols

    # def gate(self, budget0, budget, some):
    #     rows, lite, dark = 0
    #     stats, bests = {}

    #     rows = l.shuffle
    #     return 0

    # def split(self, best, rest, lite, dark):
    #     return 0

    # def bestRest(self, rows, want, best, rest, top):
    #     return 0
