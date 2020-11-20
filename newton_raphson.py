"""NEWTON RAPHSON"""

import numpy as np

def newton_raphson_x_cota(f, df, p0, cota_max, mostrar_tabla = False):

    if mostrar_tabla:
        print("Iter:", 0, " Valor:", p0, "  ", "  |pn-pn-1|:---")
    
    pn = p0
    n = 0
    cota_error = cota_max + 1
    historia=[(0,pn)]

    while cota_error > cota_max:
        n+=1
        pn_1 = pn
        pn = pn_1 - f(pn_1) / df(pn_1)
        cota_error = abs(pn - pn_1)
        resultado=(n,pn)
        historia.append(resultado)     
        

        if mostrar_tabla:
            print("Iter:", n, " Valor:", pn, "  ", "  |pn-pn-1|:", cota_error)

    return pn, n, historia
  


def newton_raphson_x_iteraciones(f, df, p0, iteraciones, mostrar_tabla = False):

    if mostrar_tabla:
        print("Iter:", 0, " Valor:", p0, "  ", "  |pn-pn-1|:---")
    
    pn = p0
    historia=np.zeros([iteraciones,2])
    historia[0]=(0,pn)
    
    for i in range(1, iteraciones):
        n=i
        pn_1 = pn
        pn = pn_1 - f(pn_1) / df(pn_1)
        cota_error = abs(pn - pn_1)
        historia[i]=(i,pn)      
        
        if mostrar_tabla:
            print("Iter:", n, " Valor:", pn, "  ", "  |pn-pn-1|:", cota_error)

    return pn,n,historia
