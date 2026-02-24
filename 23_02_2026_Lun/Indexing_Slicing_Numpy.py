import numpy as np

# Indexing e Slicing:
# Gli array NumPy possono essere indicizzati e affettati in modo simile alle liste Python, ma con funzionalità aggiuntive.
# Esempio:
print("\n--- INDEXING E SLICING BASE---\n")

arr = np. array ([1, 2, 3, 4, 5])
print(f"ARRAY: {arr}")

# Indexing
print("arr[0] ->", arr[0]) # Output: 1
# Slicing
print("arr[1:3 ->", arr[1:3]) # Output: [2 3]
# Boolean Indexing
print("arr[arr > 2] ->", arr[arr > 2]) # Output: [3 4 5]


# Indexing e Slicing:
# Gli array NumPy supportano il slicing e il fancy indexing, permettendo di estrarre porzioni di array e modificare il loro contenuto in modo efficiente.
# Esempio:

#--- SLICISNG --- :
print("\n--- SLICISNG ---\n") 
arr_slicing = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 91])
print(f"ARRAY: {arr_slicing}")

# Slicing di base
print(arr_slicing[2:7]) # Output: [2 3 4 5 6]

# Slicing con passo
print(arr_slicing[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr_slicing[:5]) # Output: [0 1 2 3 4] print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr_slicing[-5:]) # Output: [5 6 7 8 9] print(arr[:-5]) # Output: [0 1 2 3 4]

#--- FANCY INDEXING --- :
# Fancy indexing è una tecnica che permette di selezionare elementi di un array utilizzando array di indici interi.
# Questo consente una selezione complessa e flessibile di elementi rispetto allo slicing normale.
print("\n--- FANCY INDEXING ---\n") 
arr_fancy = np.array([10, 20, 30, 40, 50])
print(f"ARRAY: {arr}")

# Utilizzo di un array di indici
indices_arr = np.array ([1, 3])
print(f"Accesso con array di indici [1, 3]: {arr_fancy[indices_arr]}") # Output: [20 40]

# Utilizzo di una lista di indici
indices_arr = [0, 2, 4]
print(f"Accesso con lista [0, 2, 4]: {arr_fancy[indices_arr]}") # Output: [10 30 50]