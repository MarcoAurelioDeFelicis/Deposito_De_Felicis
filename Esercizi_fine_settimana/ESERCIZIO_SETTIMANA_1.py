from datetime import date

#env
valori = set(("char","bool","int","double","date"))
logged_user = {"utente": "stato"}
utenti = {"mirko": "M123K", "marco": "123A"}
nome_db = ""
scelte = []
data_creazione = 0
elenco_tabelle = {}

def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}\n")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper
    
def update_scelte():
    global scelte
    global logged_user
    
    scelte = ["crea_db", "exit"] if "logged_lv1" in logged_user.values() else["crea_tab","exit"]
    
    if "mirko" in logged_user.keys():
        scelte.append("crea_new_user")
        
    if len(elenco_tabelle) > 0:
        scelte.append("crea_col")
    elif "crea_col" in scelte and len(elenco_tabelle) < 1:
        scelte.pop("crea_col")
        
    if len(elenco_tabelle.items) > 0:
        scelte.append("popola")
    elif "popola" in scelte and len(elenco_tabelle.items) > 0:
        scelte.pop("popola")
        
    return scelte
    
@log_func
def registra_utente():
    print("\n --- REGISTRAZIONE UTENTE ---")
    
    while True:
        new_user = input("Scegli un nome utente: ").lower()
        
        if new_user in utenti:
            print("Errore: Questo nome utente è già esistente!\n")
            continue # Torna all'inizio del ciclo per chiedere un altro nome
        
        while True:
            new_psw = input("Scegli una password (min. 4 caratteri): ")
            if len(new_psw) > 3:
                utenti[new_user] = new_psw
                print(f"Utente {new_user} registrato con successo!")
                print(f"Utenti registrati: {len(utenti)}\n")
                return
            else:
                print("Errore: La password deve essere maggiore di 3 caratteri.\n")
                
@log_func          
def login():
    print("\n --- LOGIN ---")
    
    global logged_user
    
    while True:
        user_name = input("inserisci il tuo nome utente: ").lower()
        if user_name in utenti.keys():
            while True:
                password = input("inserisci la password: ")
                users_password = utenti.get(user_name)
                while True:
                    if password == users_password:
                        print(f"\nACCESSO EFFETT_UATO... Ciao {user_name}\n")
                        logged_user = { user_name : "logged_lv1" }
                        print(logged_user)
                        update_scelte()
                        return logged_user
                    else:
                        print("ERRORE Password errata\n")
                        break
        else:
            print("ERRORE Non sei registrato!\n") 
            
@log_func
def crea_db():
    print("\n --- CREAZIONE DB ---")
    global nome_db
    global scelte
    global logged_user
    global UserWarning
    
    if "crea_db" in scelte:
        while True:
            if nome_db == "":
                nome = input("inserisci il nome del tuo nuovo db: ")
                nome_db = nome
                data_creazione = date.today()
                # scelte.remove("crea_db")
                k, v = logged_user.popitem() 
                logged_user[k] = "logged_lv2"
                print(logged_user, "\n")
                break
            else:
                print(f"db già creato : {nome_db}")
                break
         
                
    print(f"Database '{nome_db}' creato il {data_creazione}\n")
    
@log_func    
def crea_tab():
    print("\n --- CREAZIONE TABELLA ---")
    
    while True:
        nome_tab =input("inserisci il nome della tabella da creare: ").lower()
        
        if nome_tab.isdigit():
            print("il nome deve essere una stringa")
            continue
            
        if not nome_tab  in elenco_tabelle:
            elenco_tabelle[nome_tab] = {}
        
            print(f"Tabella '{nome_tab}' creata in {nome_db}")
            print(f"Ora hai {len(elenco_tabelle)} tabelle\n")
            
            while True:
                if len(elenco_tabelle[nome_tab]) > 0:
                    altra = "altra "
                else:
                    altra = ""
                    
                proposta = input(f"vuoi aggiungere una {altra}colonna alla Tabella {nome_tab}? (y/n)\n")
                if proposta == "y":
                    crea_col(nome_tab)
                elif proposta == "n":
                    break # Esce dal ciclo delle colonne
                else:
                    print("dimmi solo 'y' o 'n' ")
            break # Esce dal ciclo delle Tabelle
        else:
            print("La tabella esiste già!\n")
            break
 
@log_func                 
def crea_col(nome_tab):
    global elenco_tabelle
    
    if nome_tab in elenco_tabelle:
        while True:
            nome_col =input(f"\ninserisci nome colonna da inserire in '{nome_tab}' o 'back' per uscire: ").lower()
            
            if not nome_col or nome_col == "back":
                break
            
            if nome_col not in elenco_tabelle[nome_tab]:
                print(f"\nTipi ammessi: {valori}")
                
                while True:
                    tipo = input(f"Inserisci tipo per {nome_col}: ").lower()
                    
                    if tipo in valori:
                        elenco_tabelle[nome_tab][nome_col] = tipo
                        print(f'Colonna "{nome_col}" ({tipo}) aggiunta a {nome_tab} con successo!\n')
                        break
                    
                    elif tipo == "back":
                        break
                    else:
                        print("Tipo non valido!")
                        continue   
            else:
                print(f"Colonna '{nome_col}' già esistente!")
                continue
            break
    else:
        print(f"Tabella non esistente {nome_tab}")

@log_func
def popola():
    if "popola" in scelte:
        pass

def play():
    login()
    
    while True:
        update_scelte()
        user = input(f"\ncosa vuoi fare? : {scelte} (").lower()
        
        if user in scelte:
            
            match user:
                case "exit":
                    exit()
                    
                case "crea_new_user":
                    registra_utente()
                    
                case "crea_db":
                    crea_db()
                    
                case "crea_tab":
                    crea_tab()
                
                case "crea_col":
                    nome_tab = input(f"in quale tabella vuoi inserire la nuova colonna? Tabelle: {elenco_tabelle.keys()} :").lower()
                    if nome_tab in elenco_tabelle.keys():
                        crea_col(nome_tab)
                    else:
                        print("ERRORE")
                    
                case _:
                    print(f"Errore: '{user}' non è tra le scelte disponibili: {scelte}")
                    continue
                    
play()