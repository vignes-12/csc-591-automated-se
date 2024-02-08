from config import *
from data import DATA

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

sorted()
print()
far()