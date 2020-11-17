import numpy as np
import matplotlib.pyplot as plt
import math

ERR = 0.02

def search_iter(a,b):
    return math.log(b - a, 2) - math.log(ERR, 2)

def set_value(a,b):
    return (a + b) / 2

def f(x):
    return ((x**2) / 4) - math.sin(x)

def calculate_root(a,b,f, iter):
    iter = 0
    num_list = []

    for i in range(0,iter):
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

# Veo que del grafico un intervalo de partida puede ser -1 y 1
# ya que en 2 la funcion vuelve a ser positiva
a = -1
b = 1
finded_iter = math.trunc(search_iter(a,b))
fun = np.vectorize(f)

x = np.linspace(a,b,finded_iter)

fig, ax = plt.subplots()
ax.plot(x, fun(x), label = "funcion")
plt.ioff()
plt.grid(True)
plt.show()
