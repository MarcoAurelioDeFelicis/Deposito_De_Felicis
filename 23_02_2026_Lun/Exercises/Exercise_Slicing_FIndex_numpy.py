# Consegna:
# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# 2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# 3. Utilizza lo slicing per estrarre gli ultimi 5 elemente dell'array.
# 4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso) .
# 5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
# 6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) 
#    assegnando loro il valore 99.
# 7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici 
# da un array più grande.

import numpy as np

arr1d = np.random.randint(10, 51, size=20)
print("ARRAY: ", arr1d)

arr_slicing = arr1d[0 : 11]
print("\nprimi 10 elementi: ", arr_slicing)

arr_slicing = arr1d[-5:]
print("\nultimi 5 elementi: ", arr_slicing)

arr_slicing = arr1d[5: 15]
print("\nda indice 5 a 15(escluso): ", arr_slicing)

arr_slicing = arr1d[0: len(arr1d): 3]
print("\nogni 3: ", arr_slicing)

modifica = arr1d[5:10] = 99
print(f"\ncon modifica ({modifica}): ", arr1d)
