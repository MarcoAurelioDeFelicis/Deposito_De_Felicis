# Consegna:
# 1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
# 2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
# 3. Inverti le righe della matrice estratta (
    # cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
# 4. Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
# 5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# 6. Stampa la matrice originale, la sotto-matrice centrale originale, estratta, la matrice invertita, 
    # la diagonale principale e la matrice invertita modificata.
    
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, 
# applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.

import numpy as np

# 1. Crea una matrice 2D 6x6 con numeri casuali tra 1 e 100
matrice_2d = np.random.randint(1, 101, size=(6, 6))
print("Matrice: \n", matrice_2d)

# 2. Estrai la sotto-matrice centrale 4x4
# indici da 1 a 5(escluso), sia per righe che per colonne
sotto_matrice = matrice_2d[1:5, 1:5]
print("\nSotto_matrice: \n", sotto_matrice)

# 3. Inverti le righe della matrice estratta
matrice_invertita = np.flip(sotto_matrice, axis=0)
# matrice_invertita = sotto_matrice[::-1, :]
print("\nmatrice_invertita: \n", matrice_invertita)

# 4. Estrai la diagonale principale della matrice invertita
diagonale_inversa = np.diag(matrice_invertita)
print("\ndiagonale_inversa: \n", diagonale_inversa)

# 5. Sostituisci i multipli di 3 con -1 nella matrice invertita
# Boolean Indexing
matrice_modificata = matrice_invertita.copy()
matrice_modificata[matrice_modificata % 3 == 0] = -1