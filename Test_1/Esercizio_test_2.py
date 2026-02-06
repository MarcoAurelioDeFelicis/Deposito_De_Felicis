# Esercizio 2:  Funzioni e Liste
# Definisca una funzione chiamata conta_vocali. 
 
#  La funzione deve: 
 
#  ricevere una stringa come parametro 
 
#  contare quante vocali contiene (a, e, i, o, u) 
 
#  restituire il numero totale di vocali 
 
#  Nel programma principale: 
 
#  chiedi all’utente di inserire una parola 
 
#  chiama la funzione 
 
#  stampa il numero di vocali trovate

def conta_vocali(stringa: str):
    vocali_trovate = [] 
    for lettera in stringa.lower():
        if lettera in ("a", "e", "i", "o", "u"):
            vocali_trovate.append(lettera)
    return len(vocali_trovate)

def play():
    parola = ""
    while True:
        user = input("inserisciuna parola: ")
        if user.isdigit():
            print("ERRORE inserisci una stringa\n")
        else:
            parola = user
            break
    risultato = conta_vocali(parola)
    print("il risultato : ", risultato, "vocali")
    
play()
        
   