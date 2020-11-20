"""NEWTON RAPHSON MODIFICADO"""

import pandas as pd
import numpy as np

ITER_MAX = 80

def newton_raphson_mod(f,df,ddf,p0,tolerancia):
    i = 1
    x = p0
    historia=[(0,x)]
    errores = []
    while i < ITER_MAX:
        x = x-(f(x)*df(x))/((df(x)**2)-f(x)*ddf(x))
        resultados=(i,x)
        historia.append(resultados)
        if abs(x - p0) < tolerancia:
            # historia= historia[:i+1]
            return x,i,historia
        errores.append(abs(x - p0))
        i += 1
        p0 = x
    return x,i,historia
