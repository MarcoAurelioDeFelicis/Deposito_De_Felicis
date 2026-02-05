# EXTRA: andare a far creare inizialmente le collezioni come tuple e poi trasformarle 
#        in lsite solo all'esigenza

import random

n = 0
while n <= 0:
    try:
        n = int(input("Inserisci un numero intero positivo n: "))
        if n <= 0:
            print("Il numero deve essere positivo. Riprova.")
    except ValueError:
        print("Per favore, inserisci un numero intero.")

    # Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
    tupla = tuple([random.randint(1, n) for _ in range(n)])
    print(f"\nTupla generata: {tupla}")

    # Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
    result_pari = tupla[0]
    for i in tupla:
        if i % 2 == 0:
            print(i)
            result_pari += i
    print(f"\nrisultato dei numeri pari :{result_pari}")
    
    # Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
    result_dispari = []
    for i in tupla:
        if i % 2 != 0:
            print(i)
            result_dispari.append(i)
    print(f"\nla lista dei dispari : {result_dispari}")
    print(f"\nLa somma di tutti i numeri dispari è: {sum(result_dispari)}")

    
    # Utilizza una funzione per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
    numeri_primi = []
    numeri_non_primi = []

    for num in tupla:
        if num < 2:
            numeri_non_primi.append(num)
        else:
            primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    primo = False
                    break
            
            if primo:
                numeri_primi.append(num)
            else:
                numeri_non_primi.append(num)
                
    print(f"il numero {n} è PRIMO?: {primo}")
    print(f"Numeri primi trovati nella lista: {numeri_primi}")
    
    # Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato
    somma_totale = sum(tupla)
    print(f"La somma di tutti i numeri è: {somma_totale}")
    print(f"La somma di tutti i numeri primi è: {sum(numeri_primi)}")
        
    somma_e_prima = True

    if somma_totale < 2:
        somma_e_prima = False
    else:
        for i in range(2, int(somma_totale**0.5) + 1):
            if somma_totale % i == 0:
                somma_e_prima = False
                break
    
    if somma_e_prima:
        print(f"Risultato: {somma_totale} è un numero primo!")
    else:
        print(f"Risultato: {somma_totale} NON è un numero primo.")
    
    

