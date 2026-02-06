# Esercizio 1:  Condizioni e cicli
# Chieda all’utente di inserire un numero intero positivo. 
 
#  Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
 
#  Per ogni numero: 
 
#  stampi "pari" se il numero è pari 
 
#  stampi "dispari" se il numero è dispari 
 
#  Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.


while True:
    val1 = input("Inserisci un intero: ")
    num1 = 0
    print(val1.isdigit())
    if val1.isdigit() == True:
        num1 = int(val1)
        if num1 <= 0:
            print("ERRORE devi inserire un numero maggiore di 0")
        else:
            num1 = int(val1)
    else:
        ("ERRORE inserisci un intero")
        
    for n in range(1,num1+1,1):
        print(n)
        if n % 2 == 0 :
            print(f"{n} PARI\n")
        else:
            print(f"{n} DISPARI\n")