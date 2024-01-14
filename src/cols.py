import re
from num import NUM
from sym import SYM

class COLS:
    def __init__(self, row):
        x, y, all = {}, {}, {}
        klass, col = 0, 0
        for at, txt in enumerate(row.cells):
            col = NUM(txt, at) if re.finditer("^[A-Z]", txt) else SYM(txt, at)
            all[at] = col
            if not re.finditer("X$", txt):
                if re.finditer("!$", txt):
                    klass = col
                (y if re.finditer("[!+-]$", txt) else x)[at] = col # TODO: make sure this works ;)
        self.x, self.y, self.all, self.klass, self.names = x, y, all, klass, row.cells

    def add(self, row):
        for cols in [self.x, self.y]:
            for _, col in cols.items():
                col.add(row.cells[col.at])
        return row

        