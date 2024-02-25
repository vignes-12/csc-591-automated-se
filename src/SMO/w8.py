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

    print("{:<30} {:<50} {:>23}".format("names", "{:<3}".format(str(data.cols.names).replace(',', '    ')), "D2h-"))

    print(f"{'mid':<30} [", end="")
    for cell in data.mid().cells:
        print(f"{cell:<13.2f}", end="")
    print(f"]     {data.mid().d2h(data):.2f}")
    
    print(f"{'div':<30} [", end="")
    for cell in data.div().cells:
        print(f"{cell:<13.2f}", end="")
    print(f"]     {data.div().d2h(data):.2f}")

    print("#")

    for i in range(20):
        stats, bests = data.gate(budget0=9, budget=4, some=0.5)
        print(f"{'smo9':<30} [", end="")
        for cell in bests[0].cells:
            print(f"{cell:<13}", end="")
        print(f"]    ") # TODO: D2H VALUES NEED TO BE CALCULATED
        # print("{:<30} {:<50} {:>15}".format("smo9", result, result.d2h(result)))

    print("#")

    for i in range(20):
        pass
        # Need to implement the random 50

filename = "../../data/auto93.csv"
repeats = 20
seed = 31210
part1(filename, seed, repeats)