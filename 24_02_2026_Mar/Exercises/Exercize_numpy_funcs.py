# Descrizione: Crea un array utilizzando linspace, 
# cambia la sua forma con reshape, 
# genera un array casuale e calcola la somma degli elementi.

# Esercizio:
# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# 2. Cambia la forma dell'array a una matrice 3x4.
# 3. Genera una matrice 3X4 di numeri casuali tra 0 e 1.
# 4. Calcola e stampa la somma degli elementi di entrambe le matrici.
import numpy as np

arr = np.linspace(0, 1, 12)
print("\narray: \n", arr)

arr_reshape = arr.reshape(3,4)
print("\narr_reshape: \n", arr_reshape)

matrice_rand = np.random.rand(3,4)
print("\nmatrice_rand: \n", matrice_rand)

somma = arr_reshape.sum() + matrice_rand.sum()
print("\nsomma: ", somma)




