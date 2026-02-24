# Crea uno script Python che esegua i seguenti passaggi:

# Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49. 
# più altre 50 posizioni casuali tra 49 e 101.

# Stampa l’array, il suo dtype e la sua shape.
# Modifica il tipo di dato (dtype) dell’array in float64.
# Verifica e stampa di nuovo dtype e shape.
# Utilizza lo slicing per ottenere:
# i primi 10 elementi
# gli ultimi 7 elementi
# gli elementi dall’indice 5 all’indice 20 escluso
# ogni quarto elemento dell'array
# Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
# Utilizza la fancy indexing per selezionare:
# gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
# tutti gli elementi pari dell’array utilizzando una maschera booleana
# tutti gli elementi maggiori della media dell'array
# Stampa:
# l’array originale dopo tutte le modifiche
# tutti i sotto-array ottenuti tramite slicing e fancy indexin

import numpy as np

arr_fissa = np.arange(50)
print("\nparte fissa : ", arr_fissa)

arr_random = np.random.randint(49, 101, size=50)
print("\nparte random 49,101 : ", arr_fissa)

arr = np.concatenate((arr_fissa, arr_random)) # oppure: arr = np.concatenate((np.arange(50), np.random.randint(
print("\narray unito : ", arr)
tipo_arr = arr.dtype
print(f"tipo dell'array : {arr.dtype}")
forma_arr=  arr.shape
print(f"fomra del'array: {forma_arr}")


tipo_arr_mod = arr.astype(np.float64)
print(f"\ntipo dell'array modificato : {tipo_arr}")
print(f"fomra del'array dopo la modifica: {forma_arr}")

# -- SliCING --
print("\n--- SliCING ---")

# i primi 10 elementi
arr_slicing = arr[0 : 11]
print("\nprimi 10 elementi: ", arr_slicing)

# gli ultimi 7 elementi
arr_slicing = arr[-7:]
print("\nultimi 5 elementi: ", arr_slicing)

# gli elementi dall’indice 5 all’indice 20 escluso
arr_slicing = arr[5: 20]
print("\nda indice 5 a 15(escluso): ", arr_slicing)

# ogni quarto elemento dell'array
arr_slicing = arr[0: len(arr): 4]
print("\nogni Quarto 4: ", arr_slicing)

# Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
modifica = arr[10:15] = 999
print(f"\ncon modifica ({modifica}): ", arr)

print("\n--- Fancy Index ---")

# gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
indices_arr = [0, 3, 7, 12, 25, 33, 48]
print(f"\nAccesso con index_list [0, 3, 7, 12, 25, 33, 48]: {arr[indices_arr]}")

# tutti gli elementi pari dell’array utilizzando una maschera booleanaù
maschera_pari = arr % 2 == 0
print("\n maschera = ", maschera_pari)
arr_pari = arr[maschera_pari]
print("\narray di numery pari con mask applicata :", arr_pari)

# tutti gli elementi maggiori della media dell'array
maschera_media = arr > np.mean(arr)
print("\nmedia dell'array", np.mean(arr))
arr_sup_media = arr[maschera_media]
print("\narray di num maggiori alla media dell'array :", arr_sup_media)