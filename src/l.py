import math
import ast
import random

def keys(t, u=None):
    if u is None:
        u = []
    for k in sorted(t.keys()):
        u.append(k)
    return u

def rnd(n, ndecs):
    if isinstance(n, int):
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** (ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def o(t, n=2, u=None):
    if isinstance(t, (int, float)):
        return str(rnd(t, n))
    if not isinstance(t, dict):
        return str(t)
    
    if u is None:
        u = []
    
    for k in [key for key in t.keys() if str(key)[0] != '_']:
        if isinstance(t[k], dict):
            if len(t[k]) > 0:
                u.append(o(t[k], n))
            else:
                u.append(f"'{o(k, n)}': {o(t[k], n)}")
        else:
            u.append(f"'{o(k, n)}': {o(t[k], n)}")

    return "{" + ", ".join(u) + "}"

def shuffle(t, j):
    u = {}
    for x in t.values():
        u.append(x)
    
    for i in range(len(u), 1, -1):
        j = random.randint(1, i) # Unsure if these are the correct bounds
        u[i], u[j] = u[j], u[i]
    
    return u

def slice(t, go, stop, inc):
    u = {}
    if go and go < 0:
        go += len(t)
    
    if stop and stop < 0:
        stop += len(t)

    for j in range((go or 1) - 1, stop or len(t), inc or 1): # Range values may need to be modified
        u.append(t[j])
    
    return u
    
        

def sort_string(input_string):
    input_dict = ast.literal_eval(input_string)
    sorted_dict = dict(sorted(input_dict.items()))
    output_string = str(sorted_dict).replace("'","")
    return output_string