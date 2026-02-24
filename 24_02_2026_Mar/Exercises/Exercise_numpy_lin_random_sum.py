# Consegna:
# 1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
# 2. Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
# 3. Somma i due array elemento per elemento per ottenere un nuovo array.
# 4. Calcola la somma totale degli elementi del nuovo array.
# 5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
# 6. Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
# 7. Salva i dati su un file TXT a ogni giro
# 8. Rendi ripetibile il processo complessivo
# 9. Chiedi se si vuole sovrascrivere il TXT o no.
# Obiettivo:
# Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, 
# random per creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array, 
# incluso l'uso di condizioni per la somma parziale e gestire il salvataggio di file in merito.
import numpy as np

def crea_arr(nome_file, mode_file):
    arrLin = np.linspace(0, 10, 50)
    print("\narraylin: \n", arrLin)
    
    arrRand = np.random.random(50) 
    print("\narrayRandom: \n", arrRand)
    
    with open(nome_file, mode_file, encoding="utf-8") as file:
        file.write(f"\n--- NUOVO GIRO ---\n")
        file.write(f"arrayLin: {arrLin.tolist()}\n")
        file.write(f"arrayRand: {arrRand.tolist()}\n")
    print("Array salvato!\n")
    
    return arrLin, arrRand

def sum_array(mode: str, arr1:np, arr2=None,):
    if mode == "sum1by1":
        sum1by1 =  arr1 + arr2
        return sum1by1
    elif mode ==  "totalsum":
        totalsum = arr1.sum()
        return totalsum
    elif mode == "sum5":
        mask = arr1 > 5 
        sum5 = arr1[mask]
        return sum5.sum()
    else: 
        print("ERRORE")
        return None
    
    
def play():
    nome_file = "mio_file.txt"
    
    while True:
        
        # 9. Chiedi se si vuole sovrascrivere il TXT
        sovrascrivi = input("\nVuoi sovrascrivere il file TXT esistente? (S/N): ").upper()
        mode_file = "w" if sovrascrivi == "S" else "a"

        # Esecuzione passaggi
        arrLin, arrRand = crea_arr(nome_file, mode_file)
        
        # Calcoli
        nuovo_array = sum_array("sum1by1", arrLin, arrRand)
        somma_tot = sum_array("totalsum", nuovo_array)
        somma_mag_5 = sum_array("sum5", nuovo_array)
        
        # 6. Stampa i risultati
        print("\n--- RISULTATI ---")
        print("Array Linspace (primi 5):", arrLin)
        print("Array Random (primi 5):  ", arrRand)
        print("Nuovo Array (somma):     ", nuovo_array)
        print(f"Somma Totale:             {somma_tot:.4f}")
        print(f"Somma elementi > 5:       {somma_mag_5:.4f}")
        
        # Salvataggio risultati finali nel file
        with open(nome_file, "a", encoding="utf-8") as file:
            file.write(f"Nuovo Array Somma: {nuovo_array.tolist()}\n")
            file.write(f"Somma Totale: {somma_tot}\n")
            file.write(f"Somma > 5: {somma_mag_5}\n")

        # Controllo uscita loop
        continua = input("\nVuoi fare un altro giro? (S/N): ").upper()
        if continua != "S":
            print("Chiusura programma.")
            break

if __name__ == "__main__":
    play()