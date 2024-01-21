from config import parse_args, the
from data import DATA
import eg
from sym import SYM
from num import NUM

def task_1(dataset):
    # for row in dataset.rows:
    #         print(row.cells)
    for col in weather.cols.x: #weatherClassCount += 1 #print("Column: ", weather.cols.x[col].txt)
        # print(f"{weather.cols.x[col].txt}'s Numbers: {weather.cols.x[col].has}")
        print(f"{weather.cols.all[col].txt:>28}")
        print("============================")

        for klassCategory in weather.cols.klass.has:
            print(f"{klassCategory:>14}", end="")
        print("\n")
        
        class_obj = weather.cols.all[col]
        if isinstance(class_obj, SYM):
            for classEntry in class_obj.has: # Can modify this to be dictionaries with values
                classEntryIndexes = []
                row_counter = 0
                class_loc = class_obj.at
                for row in dataset.rows:
                     if row.cells[class_loc] == classEntry:
                          classEntryIndexes.append(row_counter)
                     row_counter += 1
                classEntryDict = {}
                for row_number in classEntryIndexes:
                    row = dataset.rows[row_number]
                    class_entry = row.cells[dataset.cols.klass.at]
                    if class_entry not in classEntryDict:
                         classEntryDict[class_entry] = 1
                    else:
                         classEntryDict[class_entry] += 1
                for dep_var in dataset.cols.klass.has:
                    if dep_var not in classEntryDict:
                        classEntryDict[dep_var] = 0
                print(f"{classEntry:<11}", end="")
                for val in classEntryDict.values():
                    print(f"{val:>3}", end="           ")
                print()
        elif isinstance(class_obj, NUM):
            class_loc = class_obj.at
            class_obj_values = []
            for row in dataset.rows:
                 if row.cells[class_loc] not in class_obj_values:
                      class_obj_values.append(row.cells[class_loc])
            for classEntry in class_obj_values: # Can modify this to be dictionaries with values
                classEntryIndexes = []
                row_counter = 0
                class_loc = class_obj.at
                for row in dataset.rows:
                     if row.cells[class_loc] == classEntry:
                          classEntryIndexes.append(row_counter)
                     row_counter += 1
                classEntryDict = {}
                for row_number in classEntryIndexes:
                    row = dataset.rows[row_number]
                    class_entry = row.cells[dataset.cols.klass.at]
                    if class_entry not in classEntryDict:
                         classEntryDict[class_entry] = 1
                    else:
                         classEntryDict[class_entry] += 1
                for dep_var in dataset.cols.klass.has:
                    if dep_var not in classEntryDict:
                        classEntryDict[dep_var] = 0
                print(f"{classEntry:<11}", end="")
                for val in classEntryDict.values():
                    print(f"{val:>3}", end="           ")
                print()
        print("           -----------------")

        if isinstance(class_obj, SYM):
            for classEntry in class_obj.has: # Can modify this to be dictionaries with values
                classEntryIndexes = []
                row_counter = 0
                class_loc = class_obj.at
                for row in dataset.rows:
                     if row.cells[class_loc] == classEntry:
                          classEntryIndexes.append(row_counter)
                     row_counter += 1
                classEntryDict = {}
                for row_number in classEntryIndexes:
                    row = dataset.rows[row_number]
                    class_entry = row.cells[dataset.cols.klass.at]
                    if class_entry not in classEntryDict:
                        classEntryDict[class_entry] = 1
                    else:
                        classEntryDict[class_entry] += 1
                for dep_var in dataset.cols.klass.has:
                    if dep_var not in classEntryDict:
                        classEntryDict[dep_var] = 0
                print(f"{classEntry:<11}", end="")
                for key, val in classEntryDict.items():
                    if(weather.cols.all[col].txt == weather.cols.klass.txt):
                        total = 0
                        for num in weather.cols.klass.has.values():
                            total += num
                        print(f"{val}/{total:<3}", end="         ")
                    else:
                        print(f"{val}/{weather.cols.klass.has[key]:<3}", end="         ")
                print()
        elif isinstance(class_obj, NUM):
            class_loc = class_obj.at
            class_obj_values = []
            for row in dataset.rows:
                 if row.cells[class_loc] not in class_obj_values:
                      class_obj_values.append(row.cells[class_loc])
            for classEntry in class_obj_values: # Can modify this to be dictionaries with values
                classEntryIndexes = []
                row_counter = 0
                class_loc = class_obj.at
                for row in dataset.rows:
                     if row.cells[class_loc] == classEntry:
                          classEntryIndexes.append(row_counter)
                     row_counter += 1
                classEntryDict = {}
                for row_number in classEntryIndexes:
                    row = dataset.rows[row_number]
                    class_entry = row.cells[dataset.cols.klass.at]
                    if class_entry not in classEntryDict:
                         classEntryDict[class_entry] = 1
                    else:
                         classEntryDict[class_entry] += 1
                for dep_var in dataset.cols.klass.has:
                    if dep_var not in classEntryDict:
                        classEntryDict[dep_var] = 0
                print(f"{classEntry:<11}", end="")
                for key, val in classEntryDict.items():
                    if(weather.cols.all[col].txt == weather.cols.klass.txt):
                        total = 0
                        for num in weather.cols.klass.has.values():
                            total += num
                        print(f"{val}/{total:<3}", end="         ")
                    else:
                        print(f"{val}/{weather.cols.klass.has[key]:<3}", end="         ")
                print()
        print()
    for col in weather.cols.y:
        print(f"{weather.cols.y[col].txt:>28}")
        print("============================")
        for klassCategory in weather.cols.klass.has:
            print(f"{klassCategory:>14}", end="")
        print("\n")
        for val in weather.cols.klass.has.values():
            print(f"{val:>14}", end="")
        print("\n")
    print("           -----------------")
    for col in weather.cols.y:
        for klassCategory in weather.cols.klass.has:
            print(f"{klassCategory:>14}", end="")
        print("\n")
        for val in weather.cols.klass.has.values():
            print(f"{val:>11}/{len(dataset.rows)}", end="")
        print("\n")
        





weather = DATA("../data/diabetes.csv")
task_1(weather)

