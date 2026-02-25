# Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D.
# Il programma deve presentare un menu interattivo che consente all'utente di eseguire 
# varie operazioni sulla matrice. Le operazioni disponibili includono, ogni volta che il sistema
# conclude un calcolo va salvato su un file txt:

# 1. Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
# 2. Estrarre e stampare la sotto-matrice centrale.
# 3. Trasporre la matrice e stamparla.
# 4. Calcolare e stampare la somma di tutti gli elementi della matrice.
# 5. Uscire dal programma o ripetere.

#---------------------------------------------------------------------------------------------------

# Parte DUE: Andare a specializzare per aggiungere nuove operazioni:

# 6. Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una
# seconda matrice delle stesse dimensioni della elemento e stampare il risultato. 
# prima e moltiplicarle elemento per
# 7. Calcolo della Media degli Elementi della Matrice: Calcolare e stampare La media di
# tutti gli elementi della matrice.

# EXTRA:
# Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la
# matrice è quadrata).

import numpy as np
import re
import ast

def salva_su_file(nome_file, operazione, dati):
    with open(nome_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Operazione: {operazione} ---\n{dati}\n")

def crea_matrice(r,c):
    return np.random.randint(1, 101, size=(r, c))

def estrai_centro(matrice):
    r, c = matrice.shape

    if r < 3 or c < 3:
        return "Matrice troppo piccola per estrarre un centro significativo."
    centro = matrice[1:-1, 1:-1]
    return centro

def operazioni_array(mode: str, arr1:np, arr2=None,):
    if mode == "molt1by1":
        sum1by1 =  arr1 * arr2
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
    
def carica_lista_matrici(nome_file):
    matrici_trovate = []
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            contenuto = f.read()
            pattern = r"\[\[.*?\]\]"
            match = re.findall(pattern, contenuto, re.DOTALL)
            
            for m in match:
                try:
                    # Parsing str e cast in array NumPy
                    matrice_pulita = np.array(ast.literal_eval(m))
                    matrici_trovate.append(matrice_pulita)
                except:
                    continue
        return matrici_trovate
    except FileNotFoundError:
        return []

def play():
    nome_file = "matrice_log.txt"
    matrice = None
    r, c = 0, 0
    
    while True:
        if matrice is None:
            print("\n--- BENVENUTO ---")
            print("1. Crea una nuova Matrice")
            print("2. Scegli una Matrice dal file di log")
            print("0. Esci")
            scelta_iniziale = input("Cosa vuoi fare? ")

            if scelta_iniziale == '1':
                r = int(input("Inserisci numero righe: "))
                c = int(input("Inserisci numero colonne: "))
                matrice = crea_matrice(r, c)
                # salvataggio con .tolist() per poterla rileggere
                salva_su_file(nome_file, "Creazione", matrice.tolist())
                print("Matrice Creata:\n", matrice)
            
            elif scelta_iniziale == '2':
                lista = carica_lista_matrici(nome_file)
                if not lista:
                    print("Nessuna matrice trovata nel file!")
                    continue
                
                print("\n--- MATRICI DISPONIBILI NEL LOG ---")
                for i, m in enumerate(lista):
                    print(f"{i}) Matrice {m.shape}:\n{m}\n")
                
                indice = int(input("Inserisci il numero della matrice da usare: "))
                if 0 <= indice < len(lista):
                    matrice = lista[indice]
                    r, c = matrice.shape
                    print(f"Matrice {indice} selezionata.")
                else:
                    print("Indice non valido.")
            
            elif scelta_iniziale == '0':
                break
            else:
                continue
            
        print("\n--- MENU MATRICE 2D ---")
        print("2. Estrai sottomatrice centrale")
        print("3. Trasponi Matrice")
        print("4. Somma totale")
        print("5. Somma Di elementi maggiori di 5")
        print("6. Moltiplicazione Element-wise con un'altra Matrice")
        print("7. Media Elementi Matrice")
        print("9. Torna al menu principale (Cambia Matrice)")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione: ")

        if scelta == '2':
            if matrice is not None:
                centro = estrai_centro(matrice)
                print("Centro:\n", centro)
                salva_su_file(nome_file, "Sottomatrice Centrale", centro)
            else:
                print("Crea prima una matrice!")

        elif scelta == '3':
            if matrice is not None:
                trasposta = matrice.T
                print("Trasposta:\n", trasposta)
                salva_su_file(nome_file, "Trasposizione", trasposta)
            else:
                print("Crea prima una matrice!")

        elif scelta == '4':
            if matrice is not None:
                somma = operazioni_array("totalsum", matrice)
                # somma = matrice.sum()
                print("Somma totale:", somma)
                salva_su_file(nome_file, "Somma Totale", somma)
            else:
                print("Crea prima una matrice!")
                
        elif scelta == '5':
            if matrice is not None:
                somma5 = operazioni_array("sum5", matrice)
                print("Somma totale di elementi > 5:", somma5)
                salva_su_file(nome_file, "Somma totale di elementi > 5", somma5)
            else:
                print("Crea prima una matrice!")
                
        
        elif scelta == '6':
            if matrice is not None:
                matrice2 = crea_matrice(r, c)
                print("Matrice Originale:\n", matrice)
                print("Nuova Matrice:\n", matrice2)
                
                array_operato = operazioni_array("molt1by1",matrice,matrice2)
                if array_operato is not None:
                    print("Moltiplicazione tra elementi delle due matrici: \n", array_operato)
                    salva_su_file(nome_file, "Moltiplicazione tra elementi delle due matrici", array_operato)
                else:
                    print("ERRORE, operazione non valida al momento")
            else:
                print("Crea prima una matrice!")
        
        elif scelta == '7':
            if matrice is not None:
                matrice_avg = matrice.mean()
                print("Media Totale: ", matrice_avg)
                salva_su_file(nome_file, "Media Totale", matrice_avg)
            else:
                print("Crea prima una matrice!")
                
        elif scelta == '9':
            matrice = None # Reset per tornare alla scelta iniziale

        elif scelta == '0':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida.")

if __name__ == "__main__":
    play()
