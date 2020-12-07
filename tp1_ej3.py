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

S = 20
N = 6
MAX_ITER = 100
R = 4.25
VOL_PEDIDO = S / (N * 9.5)
METODO_INVALIDO = "Inválido"
METODOS = {0:"Biseccion por cota",
           1:"Punto Fijo",
           2:"Newton-Raphson",
           3:"Newton-Raphson modif.",
           4:"Secante"}
CONVERGENCIA = 3
CTE_ASINTOTICA = 4

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

def funcion_g1(x):
    return ((x**3)/(3*R)+(VOL_PEDIDO*4*R**2)/3)**(1/2)

def funcion_g2(x):
    return ((x**3)/(3*R)+(1*4*R**2)/3)**(1/2)

def calcular_cte_asintotica(p0, p1, n):
    return abs(p1) / (abs(p0) ** n)

def estimar_orden_convergencia(historia_raices,iteraciones):
    alfa = [(0,0)]

    for n in range (2,iteraciones-1):

        e_n_mas_1 = historia_raices[n+1][1]-historia_raices[n][1]
        e_n = historia_raices[n][1] - historia_raices[n-1][1]
        e_n_menos_1 = historia_raices[n-1][1] - historia_raices[n-2][1]

        alfa.append((n,np.log10(np.abs(e_n_mas_1/ e_n))/np.log10(np.abs(e_n/ e_n_menos_1))))

    return alfa

def imprimir_tabla_resultados(metodos):

    for i in range(len(metodos)):
        iteraciones = metodos[i][1]
        historial = metodos[i][2]
        convergencia = metodos[i][3]
        cte_asintotica = metodos[i][4]
        
        tabla = {}

        tabla["Historial raices"] = [elem[1] for elem in historial]
        tabla["Convergencia"] = ["-"] * len(historial) 
        tabla["Cte. Asintótica"] = ["-"] * len(historial) 

        for it, valor in convergencia:
            tabla["Convergencia"][it] = valor
        
        for it, valor in cte_asintotica:
            tabla["Cte. Asintótica"][it] = valor

        data = pd.DataFrame(tabla)

        if len(data) > 12:
            data = data[:6].append(data[-6:]) #Se queda con los primeros 6 y últimos 6 valores
        
        print(f'## Resultados {METODOS[i]} ##\n\n', data, "\n\n")

def calcular_raices(resultados):
    tabla_resultados = {}

    for cota, resul in resultados.items():
        tabla_resultados[cota] = [elem[0] for elem in resul]

    return pd.DataFrame(tabla_resultados, index = list(METODOS.values()))

def calcular_raices_brent(funciones,a,b,indice):
    raices = {"Brent": []}
    
    for f in funciones:
        raices["Brent"].append(brentq(f,a,b))
    
    return pd.DataFrame(raices, index = indice)

def graficar_orden_convergencia(resultados, valor, titulo):
    plt.figure()
    plt.grid(True)
    plt.title(titulo)

    for i in range(1, len(resultados)):
        convergencia = resultados[i][valor]
        valores_x = [elem[0] for elem in convergencia]
        valores_y = [elem[1] for elem in convergencia]
        plt.plot(valores_x,valores_y , '-', lw=2, label=METODOS[i])
        plt.legend()

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

def aplicar_metodos(f, funcion_g, a, b, tolerancia):
    resultados = []

    p0 = biseccion_x_iteracion(f, a, b, 1)[0]
    p1 = biseccion_x_iteracion(f, a, b, 2)[0]

    try: resultados.append(biseccion_x_cota(f,a,b,tolerancia))
    except ValueError: resultados.append((METODO_INVALIDO,0,0))

    resultados.append(punto_fijo(funcion_g,df,a,b,tolerancia))
    resultados.append(newton_raphson_x_cota(f,df,p0,tolerancia))
    resultados.append(newton_raphson_mod(f,df,ddf,p0,tolerancia))
    resultados.append(secante_x_cota(f,p0,p1,tolerancia))

    return resultados
  
def calcular_convergencia_cte_asintotica(metodos):
    resultados = []

    for i in range(len(metodos)):
        historial = metodos[i][2]
        iteraciones = metodos[i][1]

        cte_asintotica = []
        convergencia = estimar_orden_convergencia(historial, iteraciones)

        for it, valor in estimar_orden_convergencia(historial, iteraciones):
            cte_asintotica.append((it, calcular_cte_asintotica(historial[it][1], historial[it+1][1], valor)))

        nueva_lista = list(metodos[i])
        nueva_lista.append(convergencia)
        nueva_lista.append(cte_asintotica)

        metodos[i] = tuple(nueva_lista)

# Como la funcion es negativa en el intervalo (-inf, 0) U (9, inf)
# tomo solamente la parte positiva ya que una esfera no puede estar
# llena negativamente
# Tambien tene que estar entre 0 y 2R (no puede llenarse mas de eso)
def main():
    a = 0
    b = 2*R
    x = np.arange(a,b)

    resultados_f1 = {"1e-5":aplicar_metodos(f1,funcion_g1,a,b,1e-5),
                     "1e-13":aplicar_metodos(f1,funcion_g1,a,b,1e-13)}

    resultados_f2 = {"1e-5":aplicar_metodos(f2,funcion_g2,a,b,1e-5),
                    "1e-13":aplicar_metodos(f2,funcion_g2,a,b,1e-13)}

    raices_f1 = calcular_raices(resultados_f1)
    raices_f2 = calcular_raices(resultados_f2)

    print("\n ## Resultados f1 ## \n\n", raices_f1)
    print("\n ## Resultados f2 ## \n\n", raices_f2)

    print("\n ## Raíces por brent ## \n\n", calcular_raices_brent([f1,f2,df],a,b,["f1","f2","df"]))

    calcular_convergencia_cte_asintotica(resultados_f1["1e-5"])
    calcular_convergencia_cte_asintotica(resultados_f1["1e-13"])

    print("\n#### Cota 1e-5 ####\n")
    imprimir_tabla_resultados(resultados_f1["1e-5"])

    print("#### Cota 1e-13 ####\n") 
    imprimir_tabla_resultados(resultados_f1["1e-13"])

    graficar_orden_convergencia(resultados_f1["1e-5"],CONVERGENCIA,"Orden Convergencia f1, con cota 1e-5")
    graficar_orden_convergencia(resultados_f1["1e-13"],CONVERGENCIA,"Orden Convergencia f1, con cota 1e-13")

    graficar_orden_convergencia(resultados_f1["1e-5"],CTE_ASINTOTICA,"Cte. Asintótica f1, con cota 1e-5")
    graficar_orden_convergencia(resultados_f1["1e-13"],CTE_ASINTOTICA,"Cte. Asintótica f1, con cota 1e-13")

    graficar_funciones(x)

main()