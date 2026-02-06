from datetime import date

utenti = {"mirko": "M123K", "marco": "123A"}
scelte = ["crea_tab"]
nome_db = ""
data_creazione = 0
elenco_tabelle = [] 

def login():
    while True:
        user_name = input("inserisci il tuo nome utente: ")
        if user_name.lower() in utenti.keys():
            password = input("inserisci la password")
            if utenti.get == password:
                print(f"ACCESSO EFFETT_UATO... Ciao {user_name}")
                return user_name
            else:
                print("ERRORE Password errata")
        else:
                print("ERRORE Non sei registrato!")        
        
def log_func(funzione):
    print(f"\n---> Run di funzione : {funzione.__name__}\n")

def crea_db(nome):
    print(" --- CREAZIONE DB ---")
    global nome_db
    global data_creazione
    
    nome_db = nome
    data_creazione = date.today()
    
    print(f"Database '{nome_db}' creato il {data_creazione}")
    
def crea_tab():
    while True:
        nome_tab =input("inserisci il nome della tabella da creare: ")
        if nome_tab.isdigit():
            print("il nome deve essere una stringa")
        else:
            new_tabella = {nome_tab: {}}
            aggiunta = elenco_tabelle.append(new_tabella)
            if aggiunta:
                print(f"Tabella '{nome_tab}' creata in {nome_db}")
                print(f"Ora hai {len(elenco_tabelle)} tabelle")
            else:
                print(f"Qualcosa è andato storto")
        break
    

def play():
    login()
    user = input("cosa vuoi fare? :")
    
play()