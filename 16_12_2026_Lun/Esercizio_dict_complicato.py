# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

# from Utilities.Utility import log_func

# Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        return funzione(*args, **kwargs)
    return wrapper

@log_func
def inserisci_alunno(classe: dict):
    while True:
        cognome = input("Inserisci cognome alunno: ").strip().capitalize()
        if cognome and not cognome.isdigit():
            break
        print("ERRORE: Inserisci una stringa valido.")
        
    while True:
        voto_input = input(f"Inserisci il voto per {cognome}: ").strip()
        try:
            voto = float(voto_input)
            if 0 <= voto <= 10:
                break
            print("ERRORE: Il voto deve essere tra 0 e 10.")
        except ValueError:
            print("ERROE: Inserisci un numero valido.")

    if cognome not in classe:
        classe[cognome] = [voto]
    else: 
        classe[cognome].append(voto) 

@log_func        
def stampa_medie(classe: dict):
    if not classe:
        print("vuoto.")
        return
    
    for nome, voti in classe.items():
        media = sum(voti) / len(voti)
        print(f"Nome: {nome}, Media: {media:.1f} per voti = {voti}")

# --- Main ---
classe = {} 
        
while True:
    inserisci_alunno(classe)
    
    scelta = input("Premi 'y' per continuare, 'media' per vedere i risultati, o altro per uscire: ").lower()
    
    if scelta == 'media':
        print(classe)
        stampa_medie(classe)
        break 
    elif scelta != 'y':
        stampa_medie(classe)
        break