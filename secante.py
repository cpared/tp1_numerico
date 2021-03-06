"""Secante (metodo controlado por iteracion y por cota)"""

def secante_x_cota(f,p0, p1, cota_max, mostrar_tabla=False):
    cota_error = abs(p1 - p0)

    if mostrar_tabla:
        print("Iter:", 0, "   Valor:", p0, "    |pn - pn-1|:---")
        print("Iter:", 1, "   Valor:", p1, "    |pn - pn-1|:", cota_error)

    i = 1
    pn = p1
    pn_1 = p0
    historia=[(0,p0),(1,p1)] 
    
    while cota_error > cota_max:        
        i += 1
        pn_2 = pn_1
        pn_1 = pn 
        pn = pn_1 - f(pn_1)*(pn_1 - pn_2) / (f(pn_1) - f(pn_2)) 
        cota_error = abs(pn - pn_1)
        resultados=(i,pn)
        historia.append(resultados)

        if mostrar_tabla:
            print("Iter:", i, "   Valor:", pn, "  |pn - pn-1|:", cota_error)
        
    return pn,i,historia



def secante_x_iteracion(f,p0, p1, iteracion_max, mostrar_tabla=False):
    cota_error = abs(p1 - p0)

    if mostrar_tabla:
        print("Iter:", 0, "   Valor:", p0, "    |pn - pn-1|:---")
        print("Iter:", 1, "   Valor:", p1, "    |pn - pn-1|:", cota_error)

    pn = p1
    pn_1 = p0
    historia=np.zeros([nro_max_iteraciones,2])
    historia[0]= (0,p0)
    historia[1]=(1,p1) 

    for i in range(2, iteracion_max):
        n=1
        pn_2 = pn_1
        pn_1 = pn
        pn = pn_1 - f(pn_1)*(pn_1 - pn_2) / (f(pn_1) - f(pn_2))         
        cota_error = abs(pn - pn_1)
        resultados=(n,pn)
        historia.append(resultados)
        
        if mostrar_tabla:
            print("Iter:", i, "   Valor:", pn, "   |pn-pn-1|:", cota_error)
    
    return pn,n,historia
