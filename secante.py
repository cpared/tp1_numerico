"""Secante (metodo controlado por iteracion y por cota)"""

import numpy as np

def secante_x_cota(f,p0, p1, cota_max, mostrar_tabla=False):
    cota_error = abs(p1 - p0)

    if mostrar_tabla:
        print("Iter:", 0, "   Valor:", p0, "    |pn - pn-1|:---")
        print("Iter:", 1, "   Valor:", p1, "    |pn - pn-1|:", cota_error)

    iteracion = 1
    pn = p1
    pn_1 = p0
    valores = []
    valores.append(p0)
    valores.append(p1)
    
    while cota_error > cota_max:        
        iteracion += 1
        pn_2 = pn_1
        pn_1 = pn 
        pn = pn_1 - f(pn_1)*(pn_1 - pn_2) / (f(pn_1) - f(pn_2)) 
        cota_error = abs(pn - pn_1)
        
        valores.append(pn)

        if mostrar_tabla:
            print("Iter:", iteracion, "   Valor:", pn, "  |pn - pn-1|:", cota_error)
        
    return pn, iteracion, valores


def secante_x_iteracion(f,p0, p1, iteracion_max, mostrar_tabla=False):
    cota_error = abs(p1 - p0)

    if mostrar_tabla:
        print("Iter:", 0, "   Valor:", p0, "    |pn - pn-1|:---")
        print("Iter:", 1, "   Valor:", p1, "    |pn - pn-1|:", cota_error)

    pn = p1
    pn_1 = p0

    for i in range(2, iteracion_max):
        
        pn_2 = pn_1
        pn_1 = pn
        pn = pn_1 - f(pn_1)*(pn_1 - pn_2) / (f(pn_1) - f(pn_2)) 
        
        cota_error = abs(pn - pn_1)
        if mostrar_tabla:
            print("Iter:", i, "   Valor:", pn, "   |pn-pn-1|:", cota_error)
    
    return pn