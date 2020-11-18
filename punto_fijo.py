# -*- coding: utf-8 -*-
"""PUNTO FIJO"""

import numpy as np
import math

s= 20
n=6
K=float(s/(n*9.5))
r=4.25
nro_max_iteraciones=80

def funcion_g(x):
  return ((x**3)/(3*r)+(K*4*r**2)/3)**(1/2)

def derivada_g(x): 
  return (x**2)/(2*r*math.sqrt ((x**3)/(3*r)+(K*4*r**2)/3))

#si la grafica de g pertenece al intervalo [a,b], existe un punto fijo en el intervalo
#si la derivada de g tiene modulo menor a 1, el punto fijo es unico

def verificacion_punto_fijo (f,df,a,b):
  j=a
  while j<=b:
    y= f(j)
    if a<=y and y<=b:
      z=df(j)
      if np.abs(z)<1:
        j += 1
    else:
      return False
  return True

def punto_fijo(f, df, a, b, tolerancia):
  if not verificacion_punto_fijo(f,df, a,b):
    raise ValueError
  semilla= (a+b)/2
  historia=np.zeros([nro_max_iteraciones,2])
  historia[0]= (0,semilla)
  p_anterior=semilla
  i=1
  
  while i<nro_max_iteraciones:
    p= f(p_anterior)
    historia[i]=(i,p)
    if np.fabs((p-p_anterior)) < tolerancia:
      historia= historia[:i+1] 
      #si se llega a una raiz en una iteracion menor al numero maximo de iteraciones
      #no se consideran los valores 0 que sobran en la lista historia
      return p,i,historia
    i=i+1
    p_anterior=p
  #En el caso de que se hagan nro_max_iteraciones y no se llegue a ningun valor 
  #que verifique la condicion de paro, el metodo no se puede utilizar para obtener la raiz
  return p,i,historia

# def main():
#   a=0
#   b=2*r
#   semilla= (a+b)/2
#   tolerancia1= 1e-5
#   raiz1,iteracion1,lista1= punto_fijo(funcion_g, derivada_g, a, b, tolerancia1)
#   print('Con tolerancia= ',tolerancia1)
#   print (lista1)
#   print('La raiz obtenida a partir del metodo de punto fijo es: ', raiz1)
#   print('El numero de iteraciones necesarias son: ', iteracion1)
#   print('-------------------------------------------------------------------')
#   # tolerancia2= 1e-13
#   # raiz2,iteracion2,lista2= punto_fijo(tolerancia2)
#   # print('Con tolerancia= ',tolerancia2)
#   # print (lista2)
#   # print('La raiz obtenida a partir del metodo de punto fijo es: ', raiz2)
#   # print('El numero de iteraciones necesarias son: ', iteracion2)
# main()

# def main():
#   a=0
#   b=8.5
#   m=verificacion_punto_fijo(a,b)
#   if m==True:
#     print('Se puede utilizar el metodo de punto fijo para busqueda de raices')
#   else:
#     print('No se puede utilizar el metodo de punto fijo para busqueda de raices')

# main()

#CONVERGENCIA
def estimarOrdenConvergencia(historiaRaices,nIteraciones):
  #nIteraciones no cuenta la semilla por lo que le restamos 1
  alfa = np.zeros ((nIteraciones-1,2))
  #Necesito 4 puntos: 1 para adelante, 2 para atras y el actual con 
  #lo cual arranca en la posicion3, o sea, indice 2
  #Recordar que nIteraciones no tiene en cuenta la semilla con los cual
  #no hace falta tener en cuenta el indice 0, y se suma 1 para incluir la ultima estimacion
  for n in range (3-1,nIteraciones-1):
    e_n_mas_1 =historiaRaices[n+1][1]-historiaRaices[n][1]
    e_n=historiaRaices[n][1] - historiaRaices[n-1][1]
    e_n_menos_1= historiaRaices[n-1][1] - historiaRaices[n-2][1]

    #Falta verificar qu eno se divida por cero
    alfa[n]=m,np.log10(np.abs(e_n_mas_1/ e_n))/np.log10(np.abs(e_n/ e_n_menos_1))

  return alfa