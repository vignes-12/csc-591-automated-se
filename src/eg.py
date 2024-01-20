from data import DATA
import l
import sys
import ast

def learn(data, row, my, kl):
    my.n += 1
    kl = row.cells[data.cols.klass.at]

    if my.n > 10:
        my.tries += 1
        my.acc += 1 if kl == row.likes(my.datas) else 0
    
    my.datas[kl] = my.datas[kl] or DATA(data.cols.names)
    my.datas[kl].add(row)


# def bayes():
#     wme = {acc=0, datas={}, tries=0, n=0}


def stats():
    data = DATA("../data/auto93.csv")
    result = l.sort_string(l.o(data.stats()))
    print(result)
    result_bool = result == "{.N: 398, Acc+: 15.57, Lbs-: 2970.42, Mpg+: 23.84}"
    return result_bool

def columns():
    data = DATA("../data/auto93.csv")
    expected = 8
    actual = len(data.cols.all)
    # print(f"Expected number of columns in file: {expected}\nActual: {actual}\n")
    return expected == actual

def dependent():
    data = DATA("../data/auto93.csv")
    expected = 3
    actual = len(data.cols.y)
    # print(f"Expected number of dependent variables in file: {expected}\nActual: {actual}\n")
    return expected == actual

def independent():
    data = DATA("../data/auto93.csv")
    expected = 4
    actual = len(data.cols.x)
    # print(f"Expected number of independent variables in file: {expected}\nActual: {actual}\n")
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
    

def all(bad=0):
    bad = 0
    for k in l.keys(globals()):
        if k != "all":
            # print(k)
            if run_test(k) == False:
                bad += 1
        
    sys.stderr.write(f"{'❌ FAIL' if bad > 0 else '✅ PASS'} {bad} fail(s) \n")
    sys.exit(bad)
