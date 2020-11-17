import matplotlib.pyplot as plt
import numpy as np
import math

ERR = 0.02
DEC = 3
MAX_ITER = 100

def search_iter(a,b):
    return math.log(b - a, 2) - math.log(ERR, 2)

def set_value(a,b):
    return (a + b) / 2

def fa(x):
    if x == 0:
        x += ERR
    return x * math.cos(x) - math.log(x)

def fb(x):
    print(x)
    print(math.e)
    return (2*x) - (math.e ** (-x))

def fc(x):
    return math.e ** (-2*x) - 1 + x

def calculate_root(a,b,f):
    iter = 0
    num_list = []

    for i in range(0,MAX_ITER):
        p = set_value(a,b)
        iter += 1
        num_list.append(p)
        if f(p) > 0 and f(a) > 0:
            a = p
        else:
            b = p

        if - ERR < round(f(p), DEC) <= ERR:
            return iter, p, num_list
    return iter, None, num_list

a = 0
b = 1.6
finded_iter = math.trunc(search_iter(a,b))
iter, p, num_list = calculate_root(a,b,fc)
cad = f'Iteraciones: {iter} \n \
Raiz: {p} \n \
Lista: {num_list} \n \
f(p): {fc(p)} \n \
Iteraciones Calculadas: {finded_iter}'
print(cad)
