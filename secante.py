"""Secante (metodo controlado por iteracion y por cota)"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

R = 4.25    #Radio del tanque
N = 6       #Cantidad de iontegrantes
S = 20      #Suma ultimo digito del padron

def f(x):
  return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3*S)/(3*N*9.5))

"""
#Usar x = np.linspace(-np.pi, np.pi, 1000)
#Rango para semilla por biseccion de 0 a np.pi/2
def f(x):
    return (np.cos(x)-x)
"""

def biseccion_x_iteracion(f, a, b, iteracion_max, mostrar_tabla=False):

    if f(a)*f(b) >= 0:
        raise Exception("f(a) y f(b) deben tener diferente signo")    

    medio = (b - a)/2 + a
    
    for i in range(1, iteracion_max+1):
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        
        if mostrar_tabla:
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


def secante_x_cota(f,p0, p1, cota_max, mostrar_tabla=False):
    n = 0
    cota = abs(p1 - p0)
    p = p0
    
    while cota > cota_max:
        
        if mostrar_tabla:
            print("Iter:", n, " Valor:", p1, "  ", "  |pn-pn-1|:", cota )
        
        p = p0 - f(p0)*(p0-p1) / (f(p0)-f(p1)) 
        cota = abs(p1 - p0)
        p1 = p0
        p0 = p
        n += 1
        
    return p


def secante_x_iteracion(f,p0, p1, iteracion_max, mostrar_tabla=False):
    n = 0
    cota = abs(p1 - p0)
    p = p0
    
    for i in range(1, iteracion_max+1):
        
        if mostrar_tabla:
            print("Iter:", n, " Valor:", p1, "  ", "  |pn-pn-1|:", cota )
        
        p = p0 - f(p0)*(p0-p1) / (f(p0)-f(p1)) 
        cota = abs(p1 - p0)
        p1 = p0
        p0 = p
        n += 1

    return p


def main():
    #Graifco la funcion pedida
    x = np.linspace(-np.pi, 5, 1000)
    plt.plot(x, f(x), "blue")
    plt.show()
    
    print("Resultado optimize.brentq: ", optimize.brentq(f, 0, 4))
    #p0, i = biseccion_x_iteracion(f, 0, np.pi/2, 1)
    #p1, i = biseccion_x_iteracion(f, 0, np.pi/2, 2)
    p0, i = biseccion_x_iteracion(f, 0, 4, 1)
    p1, i = biseccion_x_iteracion(f, 0, 4, 2)
    print("P0={0}   |   P1={1}".format(p0, p1))

    #Con una cota menor a 1e-15, el denominador del cociente de la 
    #aproximacion de la derivada se va a infinito
    root = secante_x_cota(f, np.pi/4, 0.5, 1e-15, True)
    print("Secante x cota: ", root)
    
    #Con mas de 6 iteraciones (de 0 a 5), el denominador del cociente de la
    #aproximacion de la derivada se va a infinito
    root = secante_x_iteracion(f, np.pi/4, 0.5, 8, True)     
    print("Secante x iteracion: ", root)

main()