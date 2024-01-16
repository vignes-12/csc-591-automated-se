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
                csv_reader = csv.reader(input_data)
                for x in csv_reader:
                    self.add(x, fun)

        else:
            for x in src.values() if src else {}:
                self.add(x, fun)

    def add(self, t, fun, row=None):
        row = t.cells if hasattr(t, 'cells') else ROW(t)

        if self.cols:
            if fun:
                fun(self, row)

            self.rows.append(self.cols.add(row))
        else:
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
