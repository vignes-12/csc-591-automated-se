from data import DATA
from num import NUM
from sym import SYM
import l
import sys
import ast

def stats():
    data = DATA("../data/auto93.csv")
    result = l.sort_string(l.o(data.stats()))
    print(f"Stats: {result}\n")
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
    if test_name == "sym_mid":
        return sym_mid()
    if test_name == "sym_add":
        return sym_add()
    if test_name == "sym_add_mul_val":
        return sym_add_mul_val()
    

def all(bad=0):
    bad = 0
    for k in l.keys(globals()):
        if k != "all":
            # print(k)
            if run_test(k) == False:
                bad += 1
        
    sys.stderr.write(f"{'❌ FAIL' if bad > 0 else '✅ PASS'} {bad} fail(s) \n")
    sys.exit(bad)
