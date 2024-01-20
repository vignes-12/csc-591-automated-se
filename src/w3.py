from config import parse_args, the
from data import DATA
import eg

weather = DATA("../data/weather.csv")

weatherClassCount = 0
weatherRowCount = len(weather.rows)

for col in weather.cols.x: #weatherClassCount += 1 #print("Column: ", weather.cols.x[col].txt)
    weatherClassCount += 1
    # print(f"{weather.cols.x[col].txt}'s Numbers: {weather.cols.x[col].has}")
    print(f"{weather.cols.x[col].txt:>28}")
    print("============================")
    for klassCategory in weather.cols.klass.has:
        print(f"{klassCategory:>14}", end="")
    print("\n")
    
    for classEntry in weather.cols.x[col].has: # Can modify this to be dictionaries with values
        print(classEntry)
    print("\n")

# TODO:
# Find a way to link the column names with the play! column (calculation) 
# Overall just doing the math (we know how to pull the totals for class)
# Need to figure out how to aggregate conditionals (windy == TRUE and play! == yes)
print("\nWeather Klass: ", weather.cols.klass.has) 
print("Weather Class Count: ", weatherClassCount)
print("Weather Row Count: ", weatherRowCount)

# for row in weather.rows:
#     print(row.cells)

# Find the klass --> data.cols.klass (play! in weather)
# Access the possible options from klass ("yes" and "no" in weather) --> data.cols.klass.has
    

# diabetes = DATA("../data/diabetes.csv")
# soybean = DATA("../data/soybean.csv")

# diabetesClassCount = 0
# diabetesRowCount = len(diabetes.rows)

# for col in diabetes.cols.x: diabetesClassCount += 1

# print("Diabetes Klass: ", diabetes.cols.klass.has)
# print("Diabetes Class Count: ", diabetesClassCount)
# print("Diabetes Row Count: ", diabetesRowCount)



