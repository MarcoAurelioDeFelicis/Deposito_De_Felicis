# Scrivete un programma che chiede all'utente una
# serie di parole e restituisce solo le vocali e l’indice della vocale all’interno delle parole.

# Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

@log_func
def inserisci_parola():
    while True:
        valore = input("Inserisci parola: ").strip().lower()
        if valore and not valore.isdigit():
            return valore
        print("Errore: Devi inserire una parola valida.")
        
@log_func       
def stampa_vocali_e_indici(lista_parole: list):
    for parola in lista_parole:
        print(f"\nAnalisi parola: '{parola}'")
        trovate = False
        for i, lettera in enumerate(parola):
            if lettera in "aeiou":
                print(f"  - Vocale '{lettera}'indice: {i}")
                trovate = True
        if not trovate:
            print("  - Nessuna vocale trovata.")
            
    
        
lista_parole = []

while True:
    user_parola = inserisci_parola()
    lista_parole.append(user_parola)
    if input("vuoi continuare? (y/n)").lower() != 'y':
        break
    else:
        continue

print(lista_parole)
stampa_vocali_e_indici(lista_parole)
    