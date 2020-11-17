"""Bisección (algoritmo por iteraciones y por cota)"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

#Se agregan validaciones y se definen los parametros en nombre y orden, tal como
#los usa la funcion optimiza.brentq

#Hallar Intervalo
#Estimar Pasos cota error 0.02
#Calcular raiz positiva


def f(x):
    return 0.25*x**2 - np.sin(x)


def f1(x):
    return 3.25*(x-2)**3 - np.sin(x)


def biseccion_x_cota(f, a, b, cota_limite):
    
    if f(a)*f(b) >= 0:
        raise Exception("f(a) y f(b) deben tener diferente signo")
        
    medio = (b - a)/2 + a
    cota = abs(b - a)
    iteraciones = 0
    
    while cota > cota_limite:
        iteraciones += 1
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        print("Iter:{0}  |  a:{1}  |  b:{2}  |  medio:{3}  |  f(a):{4}  |  f(b):{5}  |  f(medio){6}".format(iteraciones, a, b, medio, f(a), f(b), f(medio)))
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0: return a, iteraciones
        if f_b == 0: return b, iteraciones
        if f_medio == 0: return medio, iteraciones
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
            cota = abs(a - medio)
            #print("a:{0}  |  b:{1}  |  f(a):{2}  |  f(b):{3}".format(a, b, f_a, f_b))
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a
            cota = abs(b - medio)
            #print("a:{0}  |  b:{1}  |  f(a):{2}  |  f(b):{3}".format(a, b, f_a, f_b))
            
    return medio, iteraciones


def biseccion_x_iteracion(f, a, b, iteracion_max):

    if f(a)*f(b) >= 0:
        raise Exception("f(a) y f(b) deben tener diferente signo")    

    medio = (b - a)/2 + a
    
    for i in range(1, iteracion_max+1):
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        print("Iter:{0}  |  a:{1}  |  b:{2}  |  f(a):{3}  |  f(b):{4}  |  f(medio){5}".format(i, a, b, f(a), f(b), f(medio)))
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0: return a, i
        if f_b == 0: return b, i
        if f_medio == 0: return medio, i
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
            #print("a:{0}  |  b:{1}  |  f(a):{2}  |  f(b):{3}".format(a, b, f_a, f_b))
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a
            #print("a:{0}  |  b:{1}  |  f(a):{2}  |  f(b):{3}".format(a, b, f_a, f_b))
            
    return medio, i



def main():
    #Grafico la funcion pedida
    x = np.linspace(-np.pi, np.pi, 1000)
    plt.plot(x, f(x), "blue")
    plt.show()

    cota = 0.001
    root_biseccion, iteraciones = biseccion_x_cota(f, 1, 3, cota)   
    print("**********************")
    root_biseccion, iteraciones = biseccion_x_iteracion(f, 1, 3, 10)
    print("**********************")
    root_posta =  optimize.brentq(f, 1, 3)
    print("Resultado correcto: ", root_posta)
    print("Resultado Biseccion: {0}  |   Cota: {1}  |  Iteraciones: {2}".format(root_biseccion, cota, iteraciones))


main()