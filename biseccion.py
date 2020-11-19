"""Bisección (algoritmo por iteraciones y por cota)"""

import numpy as np



def biseccion_x_cota(f, a, b, cota_limite):
    
    #Verifico el caso particular en donde la raiz esta en los extremos
    #pero no corto el algoritmo
    if f(a)==0: print("Se detecta Un valor de f(x)=0 en ", a)
    if f(b)==0: print("Se detecta Un valor de f(x)=0 en ", b)
    
    # if f(a)*f(b) >= 0:
    #     raise ValueError("f(a) y f(b) deben tener diferente signo")
        
    medio = (b - a)/2 + a
    cota = abs(b - a)
    iteraciones = 0
    valores = []
    valores.append(medio)
    
    while cota > cota_limite:
        iteraciones += 1
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0: print("Se detecta Un valor de f(x)=0 en ", a)
        if f_b == 0: print("Se detecta Un valor de f(x)=0 en ", b)
        if f_medio == 0: print("Se detecta Un valor de f(x)=0 en ", medio)
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
            cota = abs(a - medio)
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a
            cota = abs(b - medio)
            
        valores.append(medio) 

    return medio, iteraciones, valores


def biseccion_x_iteracion(f, a, b, iteracion_max):



    #Verifico el caso particular en donde la raiz esta en los extremos
    #pero no corto el algoritmo
    if f(a)==0: print("Se detecta Un valor de f(x)=0 en ", a)
    if f(b)==0: print("Se detecta Un valor de f(x)=0 en ", b)
    
    # if f(a)*f(b) >= 0:
    #     raise ValueError("f(a) y f(b) deben tener diferente signo")    
    iteraciones = 0
    medio = (b - a)/2 + a
    valores = []    
    
    for i in range(1, iteracion_max+1):
        f_a = f(a)
        f_b = f(b)
        f_medio = f(medio)
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0: 
            valores.append(0)
            return a, iteraciones, valores
        if f_b == 0: 
            valores.append(0)
            return b, iteraciones, valores
        if f_medio == 0: 
            valores.append(0)
            return medio, iteraciones, valores
        
        #Verificacion del caso limite donde la raiz cae en algun extremo
        if f_a == 0: return a, i
        if f_b == 0: return b, i
        if f_medio == 0: return medio, i
        
        if (f_a * f_medio) < 0:
            b = medio
            medio = (b - a)/2 + a
        elif (f_b * f_medio) < 0:
            a = medio
            medio = (b - a)/2 + a
            
    return medio, i