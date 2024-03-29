from data import DATA
from num import NUM
from sym import SYM
import l
import sys
import ast
import misc
from config import the

def stats():
    data = DATA("../data/auto93.csv")
    result = l.sort_string(l.o(data.stats()))
    print(f"\nStats: {result}\n")
    result_bool = result == "{.N: 398, Acc+: 15.57, Lbs-: 2970.42, Mpg+: 23.84}"
    return result_bool

def columns():
    data = DATA("../data/auto93.csv")
    expected = 8
    actual = len(data.cols.all)
    print(f"Expected number of columns in file: {expected}\nActual: {actual}\n")
    return expected == actual

def dependent():
    data = DATA("../data/auto93.csv")
    expected = 3
    actual = len(data.cols.y)
    print(f"Expected number of dependent variables in file: {expected}\nActual: {actual}\n")
    return expected == actual

def independent():
    data = DATA("../data/auto93.csv")
    expected = 4
    actual = len(data.cols.x)
    print(f"Expected number of independent variables in file: {expected}\nActual: {actual}\n")
    return expected == actual

def num_mean():
    num = NUM()
    num.add(5)
    expected = 5
    actual = num.mu
    print(f"Expected num.mean: {expected}\nActual num.mean: {actual}\n")
    return expected == actual

def num_mid():
    num = NUM()
    num.add(5)
    num.add(10)
    expected = 7.5
    actual = num.mid()
    print(f"Expected num.mid: {expected}\nActual num.mid: {actual}\n")
    return expected == actual

def num_div():
    num = NUM()
    num.add(1)
    expected = 0
    actual = num.div()
    print(f"Expected num.div: {expected}\nActual num.div: {actual}\n")
    return expected == actual

def num_like():
    num = NUM()
    num.add(15)
    num.add(25)
    expected = 0.0201
    actual = num.like(10, None)
    print(f"Expected num.like(): near .0208\nActual num.like(): {actual}\n")
    return actual - expected < .001

def sym_add():
    sym = SYM()
    sym.add("A")
    print(f"Expected sym.n: 1\nActual sym.n: {sym.n}\n")
    print(f"Expected sym.has['A']: 1\nActual sym.has['A']: {sym.has['A']}\n")
    print(f"Expected sym.mode: \"A\"\nActual sym.mode: {sym.mode}\n")
    return sym.n == 1 and sym.has['A'] == 1 and sym.mode == "A"
    
def sym_add_mul_val():
    sym = SYM()
    values = ["A", "B", "A", "C", "B", "A"]
    for value in values:
        sym.add(value)
    print(f"Expected sym.n: {len(values)}\nActual sym.n: {sym.n}\n")
    print(f"Expected sym.has[\"A\"]: 3\nActual sym.has[\"A\"]: {sym.has['A']}\n")
    print(f"Expected sym.has[\"B\"]: 2\nActual sym.has[\"B\"]: {sym.has['B']}\n")
    print(f"Expected sym.has[\"C\"]: 1\nActual sym.has[\"C\"]: {sym.has['C']}\n")
    print(f"Expected sym.mode: \"A\"\nActual sym.mode: {sym.mode}\n")
    return sym.n == len(values) and sym.has["A"] == 3 and sym.has["B"] == 2 and sym.has["C"] == 1 \
and sym.mode == 'A'

def sym_mid():
    sym = SYM()
    sym.add("A")
    expected = 0
    actual = sym.mid()
    print(f"Expected sym.mid: 0\nActual sym.mid: {actual}")
    return expected == actual

def sym_like():
    sym = SYM()
    sym.add("A")
    sym.add("B")
    sym.add("C")
    sym.add("D")
    sym.add("E")
    expected = .2286
    actual = sym.like("B", .3)
    print (f"Expected sym.like(): .2286\nActual sym.like(): {actual}\n")
    return actual - expected < .0001

def learn(data, row, my):
    my["n"] = my["n"] + 1
    kl = row.cells[data.cols.klass.at]
    if my["n"] > 10:
        my["tries"] += 1
        my["acc"] = my["acc"] + (1 if kl == row.likes(my["datas"]) else 0)
    
    if kl not in my["datas"]: my['datas'][kl] = DATA(data.cols.names)
    my['datas'][kl].add(row)

def bayes():
    wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
    DATA("../data/diabetes.csv", lambda data, t: learn(data, t, wme))
    print(wme["acc"]/wme["tries"])
    return wme["acc"]/wme["tries"] > .72

def km():
    print("#%4s\t%s\t%s" % ("acc", "k", "m"))
    k_values = [0, 1, 2, 3]
    m_values = [0, 1, 2, 3]
    for k in k_values:
        for m in m_values:
            the["k"] = k
            the["m"] = m
            wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
            DATA("../data/soybean.csv", lambda data, t: learn(data, t, wme))
            print("%5.2f\t\%s\t\%s" % (wme["acc"]/wme["tries"], k, m))

def sorted():
    print("Sorted: ")
    dataset = DATA("../data/auto93.csv")
    firstRow = dataset.rows[0]
    neighbors = firstRow.neighbors(dataset)

    for i, row in enumerate(neighbors):
        if i % 30 == 0:
            print(f"{(i+1): <8} {row.cells} {firstRow.dist(row, dataset):10.2f}")
    
def far():
    print("Far: ")
    dataset = DATA("../data/auto93.csv")

    a, b, C, evals = dataset.farapart(dataset.rows)
    print("far1: ", a.cells)
    print("far2: ", b.cells)
    print(f"distance = {C:.2f}")
    print("Evaluations: ", evals)
    
def half():
    dataset = DATA("../data/auto93.csv")
    lefts, rights, left, right, C, cut = dataset.half(dataset.rows)
    o = l.o
    print(o(len(lefts)), o(len(rights)), o(left.cells), o(right.cells), o(C), o(cut))

def tree():
    t, evals = DATA("../data/auto93.csv").tree(True)
    t.show()
    print(evals)

def branch():
    dataset = DATA("../data/auto93.csv")
    best, rest, evals = dataset.branch()
    print(l.o(best.mid().cells), l.o(rest.mid().cells))
    print(evals)

def doubletap():
    dataset = DATA("../../data/auto93.csv")
    best1, rest, evals1 = dataset.branch(32)
    best2, _, evals2 = best1.branch(4)
    print(l.o(best2.mid().cells), l.o(rest.mid().cells))
    print(evals1+evals2)

def bins():
    dataset = DATA("../data/auto93.csv")
    best, rest = dataset.branch()[:2]
    like = best.rows
    hate = l.slice(l.shuffle(rest.rows), 1, 3 * len(like))
    def score(range):
        return range.score("like", len(like), len(hate))
    t = []
    for col in dataset.cols.x:
        print()
        for range in misc._range1(col, {"LIKE":like, "HATE":hate}):
            l.oo(range)
            t.append(range)
    t = sorted(t, key=lambda x: score(x), reverse=True)
    max = score(t[0])
    print("\n#scores:\n")
    for v in l.slice(t, 1, the["B"]):
        if score(v) > max * 0.1:
            print(l.rnd(score(v)), l.o(v))
    l.oo({"LIKE":len(like), "HATE":len(hate)})

    


def run_test(test_name):
    if test_name == "stats":
        return stats()
    if test_name == "columns":
        return columns()
    if test_name == "dependent":
        return dependent()
    if test_name == "independent":
        return independent()
    if test_name == "num_mean":
        return num_mean()
    if test_name == "num_div":
        return num_div()
    if test_name == "num_mid":
        return num_mid()
    if test_name == "num_like":
        return num_like()
    if test_name == "sym_mid":
        return sym_mid()
    if test_name == "sym_add":
        return sym_add()
    if test_name == "sym_add_mul_val":
        return sym_add_mul_val()
    if test_name == "sym_like":
        return sym_like()
    if test_name == "bayes":
        return bayes()
    if test_name == "km":
        return km()
    

def all(bad=0):
    bad = 0
    for k in l.keys(globals()):
        if k != "all":
            if run_test(k) == False:
                bad += 1
        
    sys.stderr.write(f"{'❌ FAIL' if bad > 0 else '✅ PASS'} {bad} fail(s) \n")
    sys.exit(bad)