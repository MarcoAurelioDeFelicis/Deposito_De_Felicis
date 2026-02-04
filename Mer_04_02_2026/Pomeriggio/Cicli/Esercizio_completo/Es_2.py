
def ciclo(num):
    for n in range(num, -1, -1):
        print(n)
    
game_over = False
utente = input("Inserisci un numero per il countdown: ")

while not game_over:
    try:
        numero = int(utente)
        if numero <= 0:
            raise ValueError
    except ValueError:
        print("Errore! Devi inserire un numero intero positivo.")
        continue

    ciclo(numero)
        
    scelta = input("Vuoi continuare con un altro countdown? (si/no): ").lower()
    if scelta == "no":
        print("Programma terminato. Ciao!")
        game_over = True
    else: 
        print("devi scegliere tra si o no")
        
    
