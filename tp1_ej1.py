import random
import matplotlib.pyplot as plt

COMBINACION_MAX_VAL = 9999
COMBINACION_MIN_VAL = 0
EXPERIMENTO_NRO_ITER = 100000
MAX_BINS = 10000
STEP = 10

def generar_bins(max_bins, step):
    bins = []
    for i in range(0, max_bins + 1, step):
        bins.append(i)
    return bins

def generar_claves():
    combinaciones = []
    i = 0
    while i < EXPERIMENTO_NRO_ITER:
        combinacion = random.randint(COMBINACION_MIN_VAL, COMBINACION_MAX_VAL)
        i+=1
        combinaciones.append(combinacion)
    return combinaciones

def busqueda_fuerza_bruta_int(inicio_busqueda, fin_busqueda, clave):
    """
    Recibe una clave, e itera por fuerza bruta hasta encontrarla.
    Retorna el nro de iteraciones realizadas hasta llegar al valor buscado
    """
    for i in range(inicio_busqueda, fin_busqueda + 1):
        if i == clave:
            return i + 1
    return -1

def resolver_combinaciones(combinaciones):
    lista_intentos = []
    for clave in combinaciones:
        cant = busqueda_fuerza_bruta_int(COMBINACION_MIN_VAL, COMBINACION_MAX_VAL, clave)
        lista_intentos.append(cant)
    return lista_intentos

def main():
    bins = generar_bins(MAX_BINS, STEP)
    combinaciones = generar_claves()
    cant_intentos = resolver_combinaciones(combinaciones)

    plt.hist(cant_intentos, bins)
    plt.show()

main()
