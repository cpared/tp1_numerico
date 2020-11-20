"""Bisección (algoritmo por iteraciones y por cota)"""

import numpy as np

def biseccion_x_cota(f, a, b, cota_limite):
    
    if f(a)*f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener diferente signo")

    #Verifico el caso particular en donde la raiz esta en los extremos
    #pero no corto el algoritmo
    # if f(a)==0: print("Se detecta Un valor de f(x)=0 en ", a)
    # if f(b)==0: print("Se detecta Un valor de f(x)=0 en ", b)
    medio = (b - a)/2 + a     
    cota = abs(b - a)
    i = 0
    historia = [(0,medio)]
    
    while cota > cota_limite:
        i += 1
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        # if f_a == 0:
        #     resultado=(i,a)
        #     historia.append(resultado)
        #     return a,i,historia
        # if f_b == 0:
        #     resultado=(i,b)
        #     historia.append(resultado)
        #     return b,i,historia
        # if f_medio == 0:
        #     return medio,i,historia

        # if f_a == 0: print("Se detecta Un valor de f(x)=0 en ", a)
        # if f_b == 0: print("Se detecta Un valor de f(x)=0 en ", b)
        # if f_medio == 0: print("Se detecta Un valor de f(x)=0 en ", medio)
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
            cota = abs(a - medio)
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a
            cota = abs(b - medio)
        resultado=(i,medio)
        historia.append(resultado)

    return medio,i,historia


def biseccion_x_iteracion(f, a, b, iteracion_max):

    # if f(a)*f(b) >= 0:
    #     raise ValueError("f(a) y f(b) deben tener diferente signo")   

    #Verifico el caso particular en donde la raiz esta en los extremos
    #pero no corto el algoritmo
    # if f(a)==0: print("Se detecta Un valor de f(x)=0 en ", a)
    # if f(b)==0: print("Se detecta Un valor de f(x)=0 en ", b) 

    medio = (b - a)/2 + a
    historia = [(0,medio)]
    
    for i in range(1, iteracion_max+1):
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0:
            resultado=(i,a)
            historia.append(resultado)
            return a,i,historia
        if f_b == 0:
            resultado=(i,b)
            historia.append(resultado)
            return b,i,historia
        if f_medio == 0:
            return medio,i,historia
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a

        resultado=(i,medio)
        historia.append(resultado)
        
    return medio,i,historia
