from Dipendenti import *
from Porta import *

def input_validato(messaggio, tipo=str):
    while True:
        valore = input(f"{messaggio} (o '0' per annullare): ").strip()
        if valore == '0':
            return None
        if not valore:
            print("Errore: il campo non può essere vuoto.")
            continue
        try:
            return tipo(valore)
        except ValueError:
            print(f"Errore: inserire un valore di tipo {tipo.__name__}.")

def menu_principale():
    database_dipendenti = {} # Badge: Oggetto Dipendente
    porta_ufficio = Porta("Main Gate")

    while True:
        print("\n--- GESTIONALE INGRESSI ---")
        print("1. Registra nuovo Dipendente")
        print("2. Timbra Badge (Ingresso/Uscita)")
        print("3. Visualizza Log Porta")
        print("4. Esci")
        
        scelta = input("Seleziona opzione: ")

        if scelta == "1":
            print("\n-- Registrazione --")
            nome = input_validato("Nome")
            if nome is None: continue
            
            cognome = input_validato("Cognome")
            if cognome is None: continue
            
            badge = input_validato("Numero Badge", int)
            if badge is None: continue
            
            if badge in database_dipendenti:
                print("Errore: Questo numero badge è già assegnato!")
                continue

            nuovo_dip = Dipendente(nome, cognome, badge, {}, "Dipendente")
            database_dipendenti[badge] = nuovo_dip
            print(f"Successo: {nome} {cognome} registrato con badge {badge}.")

        elif scelta == "2":
            print("\n-- Terminale di Accesso --")
            badge_id = input_validato("Inserisci Badge da timbrare", int)
            if badge_id is None: continue

            if badge_id in database_dipendenti:
                dip = database_dipendenti[badge_id]
                risultato = porta_ufficio.registra_passaggio(dip)
                print(f"OK! {risultato['nominativo']} -> {risultato['azione']} alle {risultato['orario']}")
            else:
                print("Errore: Badge non trovato nel database.")

        elif scelta == "3":
            print(f"\n-- Log Accessi {porta_ufficio.nome_porta} --")
            if not porta_ufficio.storico_accessi:
                print("Nessun passaggio registrato.")
            for log in porta_ufficio.storico_accessi:
                print(f"[{log['orario']}] Badge {log['badge']}: {log['nominativo']} - {log['azione']}")
                
        elif scelta == "4":
            print("Chiusura sistema...")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu_principale()