numeri_pari_trovati = []

while len(numeri_pari_trovati) < 5:
    utente_input = input("Inserisci un numero: ")
    
    try:
        num = int(utente_input)
    except ValueError:
        print("Errore: inserisci un numero intero valido.")
        continue
    
    is_even  = False
    if num >0:
        if num % 2 == 0:
            is_even = True
            
        if is_even:
            numeri_pari_trovati.append(num)
            print(f"Il numero {num} è pari.")
        else:
            print(f"Il numero {num} è dispari.")
            
        print(f"numeri_pari_trovati: {numeri_pari_trovati}")
    else:
        print("inserisci un numero maggiore di 0")
        print(f"numeri_pari_trovati: {numeri_pari_trovati}")
