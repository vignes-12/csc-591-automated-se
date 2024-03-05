from data import DATA

def rrp():
    data = DATA("../../data/auto93.csv")
    node, evals = data.tree(True)
    node.show()
    print("evals: ", evals)

rrp()