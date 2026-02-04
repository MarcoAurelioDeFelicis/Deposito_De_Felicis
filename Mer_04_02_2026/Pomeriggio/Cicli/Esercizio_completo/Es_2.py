
def ciclo(num):
    for n in range(num, -1, -1):
        print(n)
    
game_over = False
stop = False
while not game_over:
    utente = input("Inserisci un numero per il countdown: ")
    try:
        numero = int(utente)
        if numero <= 0:
            raise ValueError
    except ValueError:
        print("Errore! Devi inserire un numero intero positivo.")
        continue
    
    while not stop:
        ciclo(numero)
            
        scelta = input("Vuoi continuare con un altro countdown? (si/no): ").lower()
        if scelta == "no":
            print("Programma terminato. Ciao!")
            stop = True
            game_over = True
        else: 
            print("devi scegliere tra si o no")
            
        
