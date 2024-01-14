b4 = {}
for k, _ in globals().items():
    b4[k] = k

l = []
the = []
help = '''

gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD−2
Learn a little, guess a lot, try the strangest guess, learn a little more, repeat

USAGE:
python gate.py [OPTIONS]

OPTIONS:
-c --cohen small effect size = .35
-f --file csv data file name = ../data/diabetes.csv
-h --help show help = false
-k --k low class frequency kludge = 1
-m --m low attribute frequency kludge = 2
-s --seed random number seed = 23408
-t --todo start up action = help

'''

# TODO refer tricks.py for help

# TODO - Do we need this ?
# Seed = 23408

# TODO - Not sure if this is correct


def isa(x, y):
    return type(y)(x)


def isclass(s, t):
    t = {'a': s}
    t['__index'] = t
    return t
