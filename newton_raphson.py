"""NEWTON RAPHSON FUNCION 1"""

import numpy as np
from scipy import optimize

R = 4.25
N = 6
S = 20
xi = 2

def f(x):
    return (np.cos(x)-x)

def df(x):
    return -np.sin(x) - 1

"""
def f(x):
    return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3*S)/(3*N*9.5))

def df(x):
    return(2*np.pi*x*R-np.pi*x**2)
"""


def newton_raphson_x_cota(f, df, p0, cota_max, mostrar_tabla = False):

    if mostrar_tabla:
        print("Iter:", 0, " Valor:", p0, "  ", "  |pn-pn-1|:---")
    
    pn = p0
    i = 0
    cota_error = cota_max + 1
    
    while cota_error > cota_max:
        i+=1
        pn_1 = pn
        pn = pn_1 - f(pn_1) / df(pn_1)
        cota_error = abs(pn - pn_1)
        
        if mostrar_tabla:
            print("Iter:", i, " Valor:", pn, "  ", "  |pn-pn-1|:", cota_error)

    return pn

    
        
def newton_raphson_x_iteraciones(f, df, p0, iteraciones, mostrar_tabla = False):

    if mostrar_tabla:
        print("Iter:", 0, " Valor:", p0, "  ", "  |pn-pn-1|:---")
    
    pn = p0
    
    for i in range(1, iteraciones):

        pn_1 = pn
        pn = pn_1 - f(pn_1) / df(pn_1)
        cota_error = abs(pn - pn_1)
        
        if mostrar_tabla:
            print("Iter:", i, " Valor:", pn, "  ", "  |pn-pn-1|:", cota_error)

    return pn



def main():
    p0 = 0.785398163 #np.pi/4;
    iteraciones = 6
    root = newton_raphson_x_cota(f, df, p0, 1e-16, True)
    print("Resultado Newton-Raphson:  ", root)
    print("Resultado optimize.brentq: ", optimize.brentq(f, 0, 4))
  
main()


"""NEWTON RAPHSON FUNCION 2"""
"""
import numpy as np
R = 4.25
N = 6
S = 20
xi = 6
def f(x):
  return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3)/(3))

def df(x):
  return(2*np.pi*x*R-np.pi*x**2)

def nr_mod(f,df,xi):
  n = 1
  error = 1e5
  x = xi
  while error > 1e-8:
    x = x-f(x)/df(x)
    error = abs(f(x))
    n += 1
  print("La raiz es: {:.4}".format(x))
  print("Las iteraciones son: {}".format(n))
def main():
  nr_mod(f,df,xi)
main()

"""