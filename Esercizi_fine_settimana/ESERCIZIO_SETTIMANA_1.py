from datetime import date

#env
logged_user = {"utente": "stato"}
utenti = {"mirko": "M123K", "marco": "123A"}
nome_db = ""
scelte = []
data_creazione = 0
elenco_tabelle = [] 

def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}\n")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper
    
def update_scelte():
    global scelte
    global logged_user
    
    scelte = ["crea_db", "exit"] if list(logged_user.values())[0] == "logged_lv1" else ["crea_tab","exit"]
    
    if "mirko" in logged_user.keys():
        scelte.append("crea_new_user")
    print(scelte)
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
    
    if "crea_db" in scelte:
        while True:
            if nome_db == "":
                nome = input("inserisci il nome del tuo nuovo db: ")
                nome_db = nome
                data_creazione = date.today()
                scelte.remove("crea_db")
                break
            else:
                print(f"db già creato : {nome_db}")
                break
         
                
    print(f"Database '{nome_db}' creato il {data_creazione}")
    
@log_func    
def crea_tab():
    print("\n --- CREAZIONE TABELLA ---")
    
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
    
    while True:
        user = input(f"\ncosa vuoi fare? : {scelte} (").lower()
        
        if user in scelte:
            
            match user:
                case "exit":
                    exit()
                case "crea_db":
                    print("DB:", nome_db)
                    crea_db()
                case "crea_tab":
                    crea_tab()
                    
                case "crea_new_user":
                    registra_utente()
                    
                case _:
                    print(f"Errore: '{user}' non è tra le scelte disponibili: {scelte}")
                    continue
                    
play()