from data import DATA
from datetime import datetime
import eg

def part1(filename, seed, repeats):
    data = DATA(filename)
    # something ova here
    print("date :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file :", filename)
    print("repeats  :", repeats)
    print("seed :", seed)
    print("rows :", len(data.rows))
    print("cols :", len(data.cols.all))
    #for i in range(0, len(data.rows)):
    #    print(data.rows[i].cells)
    #print(data.rows[i].cells for i in range(0, len(data.rows)))

    print("{:<30} {:<50} {:>15}".format("names", "{:<3}".format(str(data.cols.names).replace(',', '    ')), "D2h-"))
    # print("{:<30} {:<50} {:<7}".format("names", "['{}']".format("',   '".join(data.cols.names)), "-D2h"))
    print("{:<30} {:<50} {:>15}".format("mid", str(data.mid().cells), str(data.mid().d2h(data)))) # TODO: FIGURE OUT ROUNDING PROBLEMS/D2H
    print("{:<30} {:<50} {:>15}".format("div", str(data.div().cells), str(data.div().d2h(data)))) # TODO: FIGURE OUT ROUNDING PROBLEMS/D2H
    print("#")
    
    for i in range(20):
        best, rest = data.gate(budget0=9, budget=4, some=0.5)
        print(best)
        # print("{:<30} {:<50} {:>15}".format("smo9", result, result.d2h(result)))


filename = "../../data/auto93.csv"
repeats = 20
seed = 31210
part1(filename, seed, repeats)