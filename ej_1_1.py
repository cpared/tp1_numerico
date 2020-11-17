import numpy as np
import matplotlib.pyplot as plt
import math

ERR = 1e-5
DEC = 5
MAX_ITER = 100

def set_value(a,b):
    return (a + b) / 2

def f(x):
    return (math.e ** x) * (math.sin(x) + math.cos(x) -2*x -2)

def calculate_root(a,b):
    iter = 0
    num_list = []
    res_list = []

    for i in range(0,MAX_ITER):
        p = set_value(a,b)
        iter += 1
        num_list.append(p)
        res_list.append(f(p))
        if f(p) > 0 and f(a) > 0:
            a = p
        else:
            b = p

        if - ERR < round(f(p), DEC) <= ERR:
            return iter, p, num_list, res_list
    return iter, None, num_list

a = -2.5
b = -0.5

fig, ax = plt.subplots()
x = np.linspace(a,b,MAX_ITER)
fun = np.vectorize(f)

iter, p, num_list, res_list = calculate_root(a,b)
plt.ioff()
ax.plot(x, fun(x), label = "funcion")

plt.show()

cad = f'Iteraciones: {iter} \n \
Raiz: {p} \n \
Lista: {num_list} \n \
f(p): {f(p)}'
print(cad)
