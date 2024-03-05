from config import *
from data import DATA
import eg

def rrp():
    data = DATA("../../data/auto93.csv")
    node, evals = data.tree(True)
    node.show()
    print("evals: ", evals)

eg.doubletap()
rrp()