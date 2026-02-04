game_over = False

while not game_over:
    utente = input("Inserisci un numero per il countdown: ")
    
    try:
        numero = int(utente)
    except ValueError:
        print("Errore! Devi inserire un numero intero.")
        continue 

    for n in range(numero, -1, -1):
        print(n)
        
    scelta = input("Vuoi continuare con un altro countdown? (si/no): ").lower()
    if scelta == "no":
        print("Programma terminato. Ciao!")
        game_over = True
