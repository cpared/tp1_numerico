import numpy as np
import pandas as pd
import math

MULTIPLICADOR = 1e5

#punto (a)
def primer_metodo(a,b,c):
    x1 = ( (-b) + math.sqrt((b**2) - 4*a*c) ) / (2*a)
    x2 = ( (-b) - math.sqrt((b**2) - 4*a*c) ) / (2*a)
    return x1, x2 #retorna una tupla (x1,x2)

#punto (b)
def segundo_metodo(a,b,c):
    x1 = (-2*c) / (b + math.sqrt(b**2 - 4*a*c))
    x2 = (-2*c) / (b - math.sqrt(b**2 - 4*a*c))
    return x1, x2 #retorna una tupla (x1,x2)

def calcular_raiz(a,b,c):
    """
        Recibe los valores a,b,c correspondientes a los valores de una funcion cuadratica
        y utiliza el metodo correcto en base a si b >> a.c
    """
    if b > (a*c*MULTIPLICADOR):
        return primer_metodo(a,b,c)
    return segundo_metodo(a,b,c)

def imprimir_resultado(a,b,c):
    x1, x2 = primer_metodo(a,b,c)
    y1, y2 = segundo_metodo(a,b,c)

    data = pd.DataFrame({
                        "Primer resultado": pd.Series([x1,x2], dtype=np.dtype("float32")),
                        "Segundo resultado": pd.Series([y1,y2], dtype=np.dtype("float32")),
                        })
    
    data.index = ["x1", "x2"]

    print("\n ## Resultados ## \n\n", data)
    print("\n ## Tipos de dato trabajados ## \n\n", data.dtypes, "\n")

def main():
    a = 1
    b = 8e7
    c = 1
    imprimir_resultado(a,b,c)

main()
