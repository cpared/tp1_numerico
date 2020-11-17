"""NEWTON RAPHSON FUNCION 1"""

import numpy as np
R = 4.25
N = 6
S = 20
xi = 2
def f(x):
  return((np.pi*x**2*(3*R-x)/3)-(np.pi*4*R**3*S)/(3*N*9.5))

def df(x):
  return(2*np.pi*x*R-np.pi*x**2)

def newton_raphson(f,df,xi):
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
  newton_raphson(f,df,xi)
main()

"""NEWTON RAPHSON FUNCION 2"""

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