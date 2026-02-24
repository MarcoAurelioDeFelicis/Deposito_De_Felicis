# Esercizio 1: Somma e Media di Elementi
# Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e  100 .
# Calcolare e stampare la somma di tutti gli elementi dell'array.
# Calcolare e stampare la media di tutti gli elementi dell'array.

# Esercizio 2: Manipolazione di Array Multidimensionali
# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
# Estrarre e stampare la seconda colonna della matrice.
# Estrarre e stampare la terza riga della matrice.
# Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

# Esercizio 3: Operazioni con Fancy Indexing
# Creare un array Numpy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici 
# (0,1），（1,3），（2,2） e （3，0).
# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
# dell'array (considerando la numerazione delle righe che parte da 0).
# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.

import numpy as np

print("\n--- ES 1 ---\n")

# Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e  100 .
randarr = np.random.randint(1,100, 15)
print("random_arr: ", randarr)

# Calcolare e stampare la somma di tutti gli elementi dell'array.
randarr_sum = randarr.sum()
print("randarr_sum: ", randarr_sum)

# Calcolare e stampare la media di tutti gli elementi dell'array.
randarr_avg = randarr.mean()
print("randarr_avg: ", randarr_avg)


print("\n--- ES 2 ---\n")


# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
matrice = np.arange(1, 26).reshape(5, 5)
print("matrice 5x5: \n",matrice)

# Estrarre e stampare la seconda colonna della matrice.
seconda_colonna = matrice[:, 1] # [righe, colonne] -> [tutte le righe (:), colonna indice 1]
print("\nseconda colonna estratta: ", seconda_colonna)

# Estrarre e stampare la terza riga della matrice.
terza_riga = matrice[2, :]
print("terza_riga estratta: ", terza_riga)

# Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
somma_diagonale = np.trace(matrice)
print("somma_diagonale estratta: ", somma_diagonale)

#oppure
print("alt:")
elementi_diagonale = np.diag(matrice)
print("elementi_diagonale ", elementi_diagonale)
somma_diagonale = elementi_diagonale.sum()
print("somma_diagonale alt ", somma_diagonale)


print("\n--- ES 3 ---\n")
# Creare un array Numpy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
matrice_casuale = np.random.randint(10, 51, size=(4, 4))
print("Matrice 4x4 di interi casuali (10-50):\n" ,matrice_casuale)

# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1），（1,3），（2,2） e （3，0).
print("\nFancy indexing: ")
print(f"Al punto (0,1): {matrice_casuale[0,1]}")
print(f"Al punto (1,3): {matrice_casuale[1,3]}")
print(f"Al punto (2,2): {matrice_casuale[2,2]}")
print(f"Al punto (3,0): {matrice_casuale[3,0]}")

# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
# dell'array (considerando la numerazione delle righe che parte da 0).
maschera_odd = matrice_casuale % 2 != 0
print("\nmaschera = ", maschera_odd)
arr_odd = matrice_casuale[maschera_odd]
print("\narray di numery dispari con mask applicata :\n", matrice_casuale)

# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
scalar = 10
# Broadcasting 
result = matrice_casuale + scalar
print("\nMatrice Originale:\n" ,matrice_casuale)
print("Risultato del Broadcasting\n", result)


