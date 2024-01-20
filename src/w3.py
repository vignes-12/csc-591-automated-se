from config import parse_args, the
from data import DATA
import eg
from sym import SYM
from num import NUM

def task_1(dataset):
    for row in dataset.rows:
            print(row.cells)
    for col in weather.cols.x: #weatherClassCount += 1 #print("Column: ", weather.cols.x[col].txt)
        # print(f"{weather.cols.x[col].txt}'s Numbers: {weather.cols.x[col].has}")
        print(f"{weather.cols.x[col].txt:>28}")
        print("============================")

        for klassCategory in weather.cols.klass.has:
            print(f"{klassCategory:>14}", end="")
        print("\n")
        
        class_obj = weather.cols.x[col]
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
                print(classEntry, classEntryDict)
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
                print(classEntry, classEntryDict)
        print("\n")
    # for col in dataset.cols.x:
    #     print(f"+---------------------------+")
    #     print(f"|      Column: {dataset.cols.x[col].txt:<25}  |")
    #     print(f"+--------------+------------+")

    #     col_values = dataset.cols.x[col]
    #     if isinstance(col_values, SYM):
    #         for col_val in col_values.has:
    #             if '?' not in col_val:
    #                 print(f"| {col_val:<25} |", end="")
    #                 class_percentage = col_values.has[col_val] / len(dataset.rows) * 100
    #                 print(f" {class_percentage:.2f}%    |")
    #     elif isinstance(col_values, NUM):
    #         pass
    # print(f"+---------------------------+")
    # print(f"|      Column: {dataset.cols.klass.txt:<25}  |")
    # print(f"+--------------+------------+")
    
    # col_values = dataset.cols.klass
    # if isinstance(col_values, SYM):
    #     for col_val in col_values.has:
    #         print(f"| {col_val:<25} |", end="")
    #         class_percentage = col_values.has[col_val] / len(dataset.rows) * 100
    #         print(f" {class_percentage:.2f}%    |")
    #     print(f"+--------------+------------+")
    # elif isinstance(col_values, NUM):
    #     pass

weather = DATA("../data/diabetes.csv")
task_1(weather)

