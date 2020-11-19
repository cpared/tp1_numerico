"""NEWTON RAPHSON"""

import numpy as np

def newton_raphson_x_cota(f, df, p0, cota_max, mostrar_tabla = False):

    if mostrar_tabla:
        print("Iter:", 0, " Valor:", p0, "  ", "  |pn-pn-1|:---")
    
    pn = p0
    i = 0
    cota_error = cota_max + 1
    valores = []
    valores.append(pn)

    while cota_error > cota_max:
        i+=1
        pn_1 = pn
        pn = pn_1 - f(pn_1) / df(pn_1)
        cota_error = abs(pn - pn_1)
        valores.append(pn)

        if mostrar_tabla:
            print("Iter:", i, " Valor:", pn, "  ", "  |pn-pn-1|:", cota_error)

    return pn, i, valores
        
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