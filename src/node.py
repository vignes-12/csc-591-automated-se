import l

class NODE:
    def __init__(self, data):
        self.here = data
    
    def walk(self, fun, depth=0):
        fun(self, depth, not(self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(fun, depth + 1)
        if self.rights:
            self.rights.walk(fun, depth + 1)

    def show(self, _show, maxDepth):
        def d2h(data):
            l.rnd(data.mid().d2h(self.here))
        
        maxDepth = 0

        def _show(node, depth, leafp, post):
            nonlocal maxDepth
            post = f"{d2h(node)}\t{l.o(node.mid().cells)}" if leafp else ""
            maxDepth = max(maxDepth, depth)
            print("|.. " * depth + post)
        
        self.walk(_show)
        print("")
        print("    " * maxDepth + d2h(self.here) + l.o(self.mid().cells))
        print("    " * maxDepth + "_" + l.o(self.here.cols.names))
        
