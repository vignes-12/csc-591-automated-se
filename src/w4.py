from config import *
from data import DATA
from num import NUM
from sym import SYM
import random

BUDGET0 = 4
BUDGET = 10
SOME = 0.5

for i in range(20):
    random.seed(i)
    data = DATA("../data/auto93.csv")
    print("Seed No: ", i)
    data.gate(budget0=BUDGET0, budget=BUDGET, some=SOME)
