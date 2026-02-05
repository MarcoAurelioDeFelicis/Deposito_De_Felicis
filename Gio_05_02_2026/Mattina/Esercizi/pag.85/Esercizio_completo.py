tentativi = []
while True:
    utente = input("Inserisci un numero intero positivo: ")
    tentativi.append(int(utente))

    try:
        numero = int(utente)
        if numero <= 0:
            raise ValueError
    except ValueError:
        print("Riprova! devi inserire un numero intero positivo.\n")
        continue

    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break

    if primo:
        print(f"Il tuo numero: {numero} è PRIMO")
        # tentativi.append(utente)
    else:
        print(f"Il tuo numero: {numero} è NON primo")
        # tentativi.append(utente)

    print("\nInizio calcolo numeri pari:")
    pari = [n for n in range(1, numero) if n % 2 == 0]
    print(f"Numeri pari: {pari}")
    somma_pari = sum(pari)
    print(f"La somma dei numeri pari è: {somma_pari}")

    print("\nInizio calcolo numeri dispari:")
    dispari = [n for n in range(1, numero) if n % 2 != 0]
    print(f"Numeri dispari: {dispari}")


    while True:
        continua = input("\nVuoi inserire un altro numero? (y/n) oppure visualizzare i tentativi (visualizza): ").lower()
        if continua in ("y", "n", "visualizza"):
            break
        print("Scelta non valida, inserisci y o n.")

    if continua == "n":
        print("Programma terminato. Ciao!")
        break
    elif continua == "visualizza":
        somma_tentativi = len(tentativi)
        print(f"hai fatto:{somma_tentativi}\n i tuoi tentativ: {tentativi}")
        while True:
            continua = input("\nVuoi inserire un altro numero? (y/n)")
            if continua in ("y", "n"):
                break
            print("Scelta non valida, inserisci y o n.")
        if continua == "n":
            print("Programma terminato. Ciao!")
            break
        else:
            print("\n--- Nuova esecuzione 2 ---\n")
    else:
        print("\n--- Nuova esecuzione ---\n")
