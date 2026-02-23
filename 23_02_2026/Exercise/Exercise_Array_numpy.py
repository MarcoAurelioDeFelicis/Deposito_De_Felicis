# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) 
# e la forma (shape) dell'array.

# Esercizio:
# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array.

import numpy as np

arr = np.arange(10,49)
tipo_arr = arr.dtype
forma_arr=  arr.shape

print(arr)
print(f"tipo dell'array : {tipo_arr}")
tipo_arr = arr.astype(float)
print(f"tipo dell'array dopo la conversione : {tipo_arr}")

print(f"fomra del'array: {forma_arr}")