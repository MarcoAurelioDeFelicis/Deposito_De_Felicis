import random
from Esercizio_EXTRA import convertitore

def genera_numero(min_val, max_val):
    return random.randint(min_val, max_val)

def chiedi_uscita():
    while True:
        scelta = input("\nVuoi arrenderti? (y/n): ").lower()
        if scelta in ('y', 'n'):
            return scelta == 'y'
        print("Errore: inserisci 'y' per sì o 'n' per no.")

def gioco():
    segreto = genera_numero(1, 100)
    tentativi = []
    
    print("---> INDOVINA IL NUMERO (1-100)\n")

    while True:
        try:
            proposta = int(input("\nInserisci un numero: "))
        except ValueError:
            print("Devi inserire un numero intero!")
            continue

        tentativi.append(proposta)

        if proposta < segreto:
            print(f"Il numero {proposta} è MINORE.")
        elif proposta > segreto:
            print(f"Il numero {proposta} è MAGGIORE.")
        else:
            tentativi = convertitore(tentativi)
            print(f"BRAVO! Hai indovinato in {len(tentativi)} tentativi! tuo num:{proposta} numero da indovinare:{segreto}")
            print(f"Cronologia: {tentativi}")
            break

        if chiedi_uscita():
            print(f"Peccato! Il numero era {segreto}. Torna a trovarci!")
            break


gioco()