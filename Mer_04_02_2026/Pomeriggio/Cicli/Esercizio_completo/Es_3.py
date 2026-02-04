from .Es_4 import execute_es4
#runna con: python3 -m Mer_04_02_2026.Pomeriggio.Cicli.Esercizio_completo.Es_3

stop = False
numeri = []
quadrati = []
while stop == False:
    user = input("dimmmi un numero da inserire in lista \n")
 
    try:
        numero = int(user)
    except ValueError:
        print("Errore! Devi inserire un numero intero.")
            
    if numero :
        numeri.append(int(numero))
    print(f"lista fino ad ora {numeri}")
    
    scelta = input("vuoi aggiungere un altro numero? y - n : \n")
    if scelta.lower() == "n":
        for n in numeri:
            risultato = n * n
            # print(risultato)
            quadrati.append(risultato)
        print(f"la lista di numeri scelti: {numeri}")
        print(f"la lista di quadrati: {quadrati}\n\n")
        
        scelta = input("Vuoi eseguire l'esercizio 4? y - n : ")
        if scelta.lower() == "y":
            print("---> esecuzione ES. 4:\n")
            execute_es4(numeri)
            stop = True
        else:
            stop = True
        

    
        
            
        
    