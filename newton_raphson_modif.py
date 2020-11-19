"""NEWTON RAPHSON MODIFICADO"""

import pandas as pd
import numpy as np

ITER = 100

def newton_raphson_mod(f,df,ddf,p0,tolerancia):
    i = 1
    x = p0
    valores = []
    errores = []
    while i < ITER:
        valores.append(x)
        x = x-(f(x)*df(x))/((df(x)**2)-f(x)*ddf(x))
        if abs(x - p0) < tolerancia:
            break
        errores.append(abs(x - p0))
        p0 = x
        i += 1
    return x,i,valores