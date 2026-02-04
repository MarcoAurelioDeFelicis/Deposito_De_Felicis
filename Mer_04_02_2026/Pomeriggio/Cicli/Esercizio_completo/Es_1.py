utente = input("Inserisci un numero: ")
try:
    numero = int(utente)
except ValueError:
    print("Errore! Devi inserire un numero intero.")
    exit()
    
if int(utente) % 2 == 0 and int(utente) > 0:
    print(f"{utente} è PARI")
elif int(utente) <= 0:
   print(f"{utente} deve essere maggior e di 0")
else:
   print(f"{utente} è DISOPARI")
    