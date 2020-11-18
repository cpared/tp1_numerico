"""NEWTON RAPHSON MODIFICADO F1"""

import pandas as pd
import numpy as np

R = 4.25
N = 6
S = 20

ITER = 100
def f(x):
  return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3*S)/(3*N*9.5))

def df(x):
  return(2*np.pi*x*R-np.pi*x**2)

def ddf(x):
  return(2*np.pi*R-2*np.pi*x)

def newton_raphson_mod(f,df,ddf,a,b,tolerancia):
  n = 1
  xi = (a + b) / 2
  x = xi
  valores = []
  errores = []
  while n < ITER:
    valores.append(x)
    x = x-(f(x)*df(x))/((df(x)**2)-f(x)*ddf(x))
    if abs(x - xi) < tolerancia:
        break
    errores.append(abs(x - xi))
    xi = x
    n += 1
    return x

  #print("La raiz es: {:.50}".format(x))
  #print("El numero de iteraciones son: {}".format(n))
  #print("El error absoluto es: {:.50}".format(error))
  # data = pd.DataFrame({
  #   "P": pd.Series(valores,
  #   "error": pd.Series(errores)
  # })
  # print(data)


# def main():
#   newton_raphson_mod(f,df,ddf)
# main()

# """NEWTON RAPHSON MODIFICADO F2"""
#
# import numpy as np
# R = 4.25
# N = 6
# S = 20
# xi = 50000000000
# def f2(x):
#   return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3)/(3))
#
# def df2(x):
#   return(2*np.pi*x*R-np.pi*x**2)
#
# def ddf2(x):
#   return(2*np.pi*R-2*np.pi*x)
#
# def newton_raphson_mod(f2,df2,ddf2):
#   n = 1
#   error = 1e5
#   x = xi
#   while error > 1e-8:
#     x = x-(f2(x)*df2(x))/((df2(x)**2)-f2(x)*ddf2(x))
#     error = abs(f2(x))
#     n += 1
#   print("La raiz es: {:.4}".format(x))
#   print("Las iteraciones son: {}".format(n))
#
# def main():
#   newton_raphson_mod(f2,df2,ddf2)
# main()

R = 4.25
N = 6
S = 20
xi = 50000000000
def f2(x):
  return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3)/(3))

def df2(x):
  return(2*np.pi*x*R-np.pi*x**2)

def ddf2(x):
  return(2*np.pi*R-2*np.pi*x)

# def newton_raphson_mod(f2,df2,ddf2):
#   n = 1
#   error = 1e5
#   x = xi
#   while error > 1e-8:
#     x = x-(f2(x)*df2(x))/((df2(x)**2)-f2(x)*ddf2(x))
#     error = abs(f2(x))
#     n += 1
#   print("La raiz es: {:.4}".format(x))
#   print("Las iteraciones son: {}".format(n))
# def main():
#   newton_raphson_mod(f2,df2,ddf2)
# main()