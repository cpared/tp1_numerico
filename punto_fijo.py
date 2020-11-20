# -*- coding: utf-8 -*-
"""PUNTO FIJO"""

import numpy as np

nro_max_iteraciones=80

#si la grafica de g pertenece al intervalo [a,b], existe un punto fijo en el intervalo
#si la derivada de g tiene modulo menor a 1, el punto fijo es unico

def punto_fijo(f, df, a, b, tolerancia):
  semilla= (a+b)/2
  historia= []
  historia.append((0,semilla))
  p_anterior=semilla
  i=1
  
  while i<nro_max_iteraciones:
    p= f(p_anterior)
    historia.append((i,p))
    if np.fabs((p-p_anterior)) < tolerancia:
      #si se llega a una raiz en una iteracion menor al numero maximo de iteraciones
      #no se consideran los valores 0 que sobran en la lista historia
      return p,i,historia
    i=i+1
    p_anterior=p
  #En el caso de que se hagan nro_max_iteraciones y no se llegue a ningun valor 
  #que verifique la condicion de paro, el metodo no se puede utilizar para obtener la raiz
  return p,i,historia