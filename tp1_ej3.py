import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.optimize import brentq
from biseccion import biseccion_x_cota, biseccion_x_iteracion
from punto_fijo import punto_fijo
from newton_raphson import newton_raphson_x_cota
from newton_raphson_modif import newton_raphson_mod
from secante import secante_x_cota
from convergencia import estimar_orden_convergencia

S = 20
N = 6
MAX_ITER = 100
R = 4.25
VOL_PEDIDO = S / (N * 9.5)
METODO_INVALIDO = "Inválido"

def funcion_h_agua(x):
    return ( np.pi * (x**2) * (3*R - x) ) / 3

def f1(x):
  return funcion_h_agua(x) - (funcion_h_agua(2*R) * VOL_PEDIDO)

def f2(x):
  return funcion_h_agua(x) - funcion_h_agua(2*R) #No multiplica por nada, porque 100% equivale a multiplicar por 1

def df(x):
    return (2*np.pi * x*R) - (np.pi * (x**2))

def ddf(x):
  return(2*np.pi*R-2*np.pi*x)

def funcion_g(x):
  return ((x**3)/(3*R)+(VOL_PEDIDO*4*R**2)/3)**(1/2)

def calcular_cte_asintotica(p0, p1, n):
    return abs(p1) / (abs(p0) ** n)

def calcular_raices(f, funcion_g, a, b):

    tabla_resultados = {"1e-5": [], "1e-13": []}

    for tolerancia, resultados in tabla_resultados.items():
        tolerancia_num = float(tolerancia)
        p0, i = biseccion_x_iteracion(f, a, b, 1)
        p1, i = biseccion_x_iteracion(f, a, b, 2)

        try: resultados.append(brentq(f,a,b))
        except ValueError: resultados.append(METODO_INVALIDO)

        try: resultados.append(biseccion_x_cota(f,a,b,tolerancia_num)[0])
        except ValueError: resultados.append(METODO_INVALIDO)

        try: resultados.append(punto_fijo(funcion_g,df,a,b,tolerancia_num)[0])
        except ValueError: resultados.append(METODO_INVALIDO)

        try: resultados.append(newton_raphson_x_cota(f,df,p0,tolerancia_num)[0])
        except ValueError: resultados.append(METODO_INVALIDO)

        try: resultados.append(newton_raphson_mod(f,df,ddf,p0,tolerancia_num)[0])
        except ValueError: resultados.append(METODO_INVALIDO)

        try: resultados.append(secante_x_cota(f,p0,p1,tolerancia_num)[0])
        except ValueError: resultados.append(METODO_INVALIDO)

    data = pd.DataFrame(tabla_resultados)

    data.index = ["Brent","Biseccion por cota","Punto Fijo","Newton-Raphson","Newton-Raphson modif.","Secante"]

    return data

def graficar_cte_asintotica(data):
    pass


def graficar_orden_convergencia(a,b):
    # p0, i1 = biseccion_x_iteracion(f1, a, b, 1)
    # p1, i2 = biseccion_x_iteracion(f1, a, b, 2)
    # n, i3, historialRaices = secante_x_cota(f2,p0,p1,1e-5)

    p0, i, historial_raices = punto_fijo(funcion_g,df,a,b,1e-5)
    ordenConvergenciaPuntoFijo = estimar_orden_convergencia(historial_raices, i)

    plt.figure()
    plt.grid(True)
    plt.plot(ordenConvergenciaPuntoFijo[:,0], ordenConvergenciaPuntoFijo[:,1], '-', lw=2, label="Punto Fijo")

def graficar_funciones(x):
    fig, ax = plt.subplots()

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    ax.plot(x,f1(x), label="Vol pedido")
    ax.plot(x,f2(x), label="Vol Max")
    ax.plot(x, df(x), label="Derivada")
    ax.set_title("Volumen")
    ax.legend()
    plt.show()

# Como la funcion es negativa en el intervalo (-inf, 0) U (9, inf)
# tomo solamente la parte positiva ya que una esfera no puede estar
# llena negativamente
# Tambien tene que estar entre 0 y 2R (no puede llenarse mas de eso)
def main():
    a = 0
    b = 2*R
    x = np.arange(a,b)

    print("\n ## Resultados f1 ## \n\n", calcular_raices(f1, funcion_g, a, b))
    print("\n ## Resultados f2 ## \n\n", calcular_raices(f2, funcion_g, a, b))

    graficar_orden_convergencia(a,b)
    graficar_funciones(x)

main()
