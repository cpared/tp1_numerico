import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import pandas as pd

S = 20
N = 6
MAX_ITER = 100
R = 4.25
VOL_PEDIDO = S / (N * 9.5)

def funcion_h_agua(x):
    return ( np.pi * (x**2) * (3*R - x) ) / 3

def f(x, vol_pedido):
    return funcion_h_agua(x) - (funcion_h_agua(2*R) * vol_pedido)

def f1(x):
  return funcion_h_agua(x) - (funcion_h_agua(2*R) * VOL_PEDIDO)

def f2(x):
  return funcion_h_agua(x) - funcion_h_agua(2*R) #No multiplica por nada, porque 100% equivale a multiplicar por 1

def derivada_f(x):
    return (2*np.pi * x*R) - (np.pi * (x**2))

def calcular_cte_asintotica():
    pass

# Como la funcion es negativa en el intervalo (-inf, 0) U (9, inf)
# tomo solamente la parte positiva ya que una esfera no puede estar
# llena negativamente
# Tambien tene que estar entre 0 y 2R (no puede llenarse mas de eso)
def main():
    a = 0
    b = 2*R
    fig, ax = plt.subplots()
    x = np.arange(a,b)

    resultados = {
                    "Brent": [brentq(f1,a,b), brentq(f2,a,b), brentq(derivada_f,a,b)],
                    "Biseccion": [0,0,0],
                    "Punto Fijo": [0,0,0],
                    "Newton-Raphson": [0,0,0],
                    "Newton-Raphson modif.": [0,0,0],
                    "Secante": [0,0,0]
                 }

    data = pd.DataFrame(resultados)
    data.index = ["f1", "f2", "df"]
    print("\n ## Resultados ## \n\n", data)

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
