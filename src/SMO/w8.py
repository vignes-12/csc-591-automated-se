from data import DATA
from datetime import datetime
from row import ROW
import eg
import random

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
        stats, bests = data.gate(budget0=4, budget=9, some=0.5)
        best = bests[-1]
        print(f"{'smo9':<30} [", end="")
        for cell in best.cells:
            print(f"{cell:<13}", end="")
        print(f"]     {best.d2h(data):.2f}") 

    print("#")

    for i in range(20):
        selectRows = random.sample(data.rows, 50)
        minRow = min(selectRows, key=lambda row:row.d2h(data))

        print(f"{'any50':<30} [", end="")
        for cell in minRow.cells:
            print(f"{cell:<13}", end="")
        print(f"]     {minRow.d2h(data):.2f}")
    
    print("#")

    globalMin = min(data.rows, key=lambda row: row.d2h(data))
    print(f"{'100%':<30} [", end="")
    for cell in globalMin.cells:
        print(f"{cell:<13}", end="")
    print(f"]     {globalMin.d2h(data):.2f}")


filename = "../../data/auto93.csv"
repeats = 20
seed = 31210
part1(filename, seed, repeats)