from row import ROW
from cols import COLS
import csv
from config import l

class DATA:
    def __init__(self, src, fun=None):
        self.rows = {}
        self.cols = None

        if isinstance(src, str):
            with open(src, "r") as input_data:
                csv_reader = csv.reader(input_data)
                for x in csv_reader:
                    self.add(x, fun)
        
        else:
            for idx, x in enumerate(src) if src else {}:
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
        u= {}

        for col in cols.items() if cols else self.cols.all.items():
            u.append(col.mid())
        
        return ROW(u)
    
    def div(self, cols, u):
        u= {}

        for col in cols.items() if cols else self.cols.all.items():
            u.append(col.div())
        
        return ROW(u)
    
    # def small(self, u):
    #     u = {}

    #     for col in self.cols.all.items():
    #         u.append(col.small())

    #     return ROW(u)
    
    # def stats(self, cols, fun, ndivs, u):
    #     u = {[".N"] : len(self.rows)}

    #     for col in self.cols[cols].values if self.cols[cols] else self.cols["y"]:
    #         # u[col.txt] = l.rnd(getmetatable(col)[fun or "mid"](col), ndivs) TODO: Figure this out once config is created
    #         pass

    #     return u        
    
    # def gate(self, budget0, budget, some):
    #     rows, lite, dark = 0
    #     stats, bests = {}

    #     rows = l.shuffle
    #     return 0
    
    # def split(self, best, rest, lite, dark):
    #     return 0
    
    # def bestRest(self, rows, want, best, rest, top):
    #     return 0