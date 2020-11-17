import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

S = 20
N = 6
MAX_ITER = 100
R = 4.25
VOL_PEDIDO = S / (N * 9.5)

def funcion_h_agua(x):
    return ( np.pi * (x**2) * (3*R - x) ) / 3

def f(x, vol_pedido):
    return funcion_h_agua(x) - (funcion_h_agua(2*R) * vol_pedido)

def derivada_f(x):
    return (2*np.pi * x*R) - (np.pi * (x**2))

def calcular_cte_asintotica():
    pass

# Como la funcion es negativa en el intervalo (-inf, 0) U (9, inf)
# tomo solamente la parte positiva ya que una esfera no puede estar
# llena negativa
# Tambien tene que estar entre 0 y 2R (no puede llenarse mas de eso)
def main():
    a = 0
    b = 2*R
    fig, ax = plt.subplots()
    x = np.arange(a,b)
    cad = f'Raiz: {optimize.brentq(funcion_h_agua,a,b)}'

    print(cad)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    ax.plot(x,f(x, VOL_PEDIDO), label="Vol pedido")
    ax.plot(x,f(x, 1), label="Vol Max")
    ax.plot(x, derivada_f(x), label="Derivada")
    ax.set_title("Volumen")
    ax.legend()
    plt.show()

main()
