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
            if not txt.endswith("$"): #if not re.finditer("X$", txt):
                if txt.endswith("!"): #if re.finditer("!$", txt):
                    klass = col
                # (y if re.finditer("[!+-]$", txt) else x)[at] = col # TODO: make sure this works ;)
                # if(re.finditer("[!+-]$", txt)):
                if(txt.endswith("!") or txt.endswith("+") or txt.endswith("-")):
                    y[at] = col
                else:
                    x[at] = col
        self.x, self.y, self.all, self.klass, self.names = x, y, all, klass, row.cells

    def add(self, row):
        for cols in [self.x, self.y]:
            for _, col in cols.items():
                print("Col: ", col.txt)
                print("Row: ", row.cells)
                col.add(row.cells[col.at])
        return row

        