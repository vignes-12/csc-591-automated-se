import re
import num
import sym

class COLS:
    def __init__(self, row):
        x, y, all = [], [], {}
        klass, col = 0, 0
        for at, txt in row.cells.items():
            col = num(txt, at) if re.finditer("^[A-Z]", txt) else sym(txt, at)
            all.append(col)
            if not re.finditer("X$", txt):
                if re.finditer("!$", txt):
                    klass = col
                (y if re.finditer("[!+-]$", txt) else x)[at] = col # TODO: make sure this works ;)
        self.x, self.y, self.all, self.klass, self.names = x, y, all, klass, row.cells

    def add(self, row):
        for _, cols in [self.x, self.y]:
            for _, col in cols.items():
                col.add(row.cells[col.at])
        return row

        