from data import DATA
import l
import sys
import ast

def stats():
    data = DATA("../data/auto93.csv")
    result = l.sort_string(l.o(data.stats()))
    print(result)
    result_bool = result == "{.N: 398, Acc+: 15.57, Lbs-: 2970.42, Mpg+: 23.84}"
    return result_bool

def columns(data):
    expected = 8
    actual = len(data.cols.all)
    print(f"Expected number of columns in file: {expected}\nActual: {actual}\n")
    return expected == actual

def dependent(data):
    expected = 3
    actual = len(data.cols.y)
    print(f"Expected number of dependent variables in file: {expected}\nActual: {actual}\n")
    return expected == actual

def independent(data):
    expected = 4
    actual = len(data.cols.x)
    print(f"Expected number of independent variables in file: {expected}\nActual: {actual}\n")
    return expected == actual

def run_test(test_name):
    if test_name == "stats":
        return stats()
    data = DATA("../data/auto93.csv")
    if test_name == "columns":
        return columns(data)
    if test_name == "dependent":
        return dependent(data)
    if test_name == "independent":
        return independent(data)
    

def all(bad=0):
    bad = 0
    for k in l.keys(globals()):
        if k != "all":
            print(k)
            if run_test(k) == False:
                bad += 1
        
    sys.stderr.write(f"{'❌ FAIL' if bad > 0 else '✅ PASS'} {bad} fail(s) \n")
    sys.exit(bad)
