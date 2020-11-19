import numpy as np

def estimar_orden_convergencia(historia_raices,iteraciones):
  alfa = np.zeros ((iteraciones-1,2))

  for n in range (2,iteraciones-1):

    e_n_mas_1 = historia_raices[n+1][1]-historia_raices[n][1]
    e_n = historia_raices[n][1] - historia_raices[n-1][1]
    e_n_menos_1 = historia_raices[n-1][1] - historia_raices[n-2][1]

    alfa[n]=n,np.log10(np.abs(e_n_mas_1/ e_n))/np.log10(np.abs(e_n/ e_n_menos_1))

  return alfa