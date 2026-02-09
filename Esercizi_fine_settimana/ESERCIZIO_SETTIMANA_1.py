# TODO: [1.validazione di bool non va]
#DB: {'Pizzeria': {'pizza': [['margherita', 8.0], ['rossa', 5.0]]}}

from datetime import date
import re

#env
valori = set(("char","bool","int","double","date")) #TODO: ,"auto_increment" da sistemare
logged_user = {"utente": "stato"}
utenti = {"mirko": "M123K", "marco": "123A"}
nome_db = ""
scelte = []
data_creazione = 0
schema_tabelle = {}
db = {}

def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}\n")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

def update_scelte(livello: str):
    global scelte
    global logged_user
    
    if livello:
        k = next(iter(logged_user))
        logged_user[k] = livello

    # Reset scelte base
    if "logged_lv3" in logged_user.values():
        scelte = ["back", "create", "read"]
        if any(len(righe) > 0 for righe in db.get(nome_db, {}).values()):
            if "update" not in scelte: scelte.append("update")
            if "delete" not in scelte: scelte.append("delete")
        return scelte
    
    elif "logged_lv1" in logged_user.values():
        scelte = ["exit", "crea_db"]
        
    elif "logged_lv2" in logged_user.values():
        scelte = ["exit", "crea_tab"]
        
    # Aggiunte dinamiche
    if "mirko" in logged_user:
        scelte.append("crea_new_user")
        
    if schema_tabelle: # Se ci sono tabelle
        if "crea_col" not in scelte: scelte.append("crea_col")
        
        # popola solo se almeno una tabella ha almeno una colonna
        if any(len(col) > 0 for col in schema_tabelle.values()):
            if "popola" not in scelte: scelte.append("popola")
            
    elif "crea_col" in scelte and len(schema_tabelle) < 1:
        scelte.pop("crea_col")
            
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
                        logged_user = { user_name : "logged_lv1" } #inizializza lo stato per l'user corrente
                        update_scelte("")
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
    global db
    
    if "crea_db" in scelte:
        while True:
            if nome_db == "":
                nome = input("inserisci il nome del tuo nuovo db: ")
                if not nome.isdigit():
                    nome = nome.capitalize()
                nome_db = nome
                data_creazione = date.today()
                db[nome_db] = {}
                # scelte.remove("crea_db")
                update_scelte("logged_lv2")
                break
            else:
                print(f"db già creato : {nome_db}")
                break
         
                
    print(f"Database '{nome_db}' creato il {data_creazione}\n")
    
@log_func    
def crea_tab():
    print("\n --- CREAZIONE TABELLA ---")
    global db
    
    while True:
        nome_tab =input("inserisci il NOME della TABELLA da creare: ").lower()
        
        if nome_tab.isdigit():
            print("il nome deve essere una stringa")
            continue
            
        if not nome_tab  in schema_tabelle:
            schema_tabelle[nome_tab] = {}
            db[nome_db][nome_tab] = []
            print(f" DB -- {db}")
        
            print(f"Tabella '{nome_tab}' creata in {nome_db}")
            print(f"Ora hai {len(schema_tabelle)} tabelle\n")
            
            while True:
                altra = "altra " if len(schema_tabelle[nome_tab]) > 0 else ""
                    
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
def crea_col(nome_tab: str):
    global schema_tabelle
    
    if nome_tab in schema_tabelle:
        while True:
            nome_col =input(f"\ninserisci NOME COLONNA da inserire in '{nome_tab}' o 'back' per uscire: ").lower()
            
            if not nome_col:
                continue
            elif nome_col == "back":
                break
                
            
            if nome_col not in schema_tabelle[nome_tab] and nome_col != "":
                # if not nome_col == "id" and schema_tabelle[nome_tab] <= 0:
                #     schema_tabelle[nome_tab]["id"] = "auto_increment"
                #     print("")
                    
                print(f"\nTipi ammessi: {valori}")
                
                while True:
                    tipo = input(f"Inserisci 'back' per uscire o TIPO per {nome_col}: ").lower()
                    
                    if tipo in valori:
                        schema_tabelle[nome_tab][nome_col] = tipo
                        print(f'Colonna "{nome_col}" ({tipo}) aggiunta a {nome_tab} con successo!')
                        print(f"Schema aggiornato {nome_tab} : {schema_tabelle[nome_tab]}\n")
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
        
def view_tab(nome_tab, schema_tab):
    if not nome_tab in db[nome_db]:
        print("ERRORE: nessuna tabella o tabella inesistente")
        return 
        
    headers = ["id_row"] + list(schema_tab.keys())
    print(" | ".join(headers))
    print("-" * (len(headers) * 12)) # Linea proporzionale alle colonne
    
    for i, riga in enumerate(db[nome_db][nome_tab], start=0):
        record_con_id = [i] + riga
        print(" | ".join(map(str, record_con_id)))
    print("\n")

        
def valida(crud: str, user: str, schema_tab: dict, nome_tab=None, id_row=None):
    def valida_char(valore: str):
        valore = valore.strip().lower()
        if not valore.isdigit():
            return str(valore)
        else:
            return False
        
    def valida_int(valore: str):
        valore = valore.strip()
        if valore.isdigit():
            return int(valore)
        else:
            return False
        
    def valida_bool(valore: str):
        valore = valore.strip()
        if valore in ("true", "1", "t", "si", "yes"):
            return "True"
        elif valore in ("false", '0', "f", "no"):
            return "False"
        return "not_bool"
        
    def valida_double(valore: str):
        valore = valore.strip().replace(",", ".")
        if "." in valore:
            parti = valore.split(".")
            # print("DEBUG", parti)
            if len(parti) == 2 and parti[0].isdigit() and parti[1].isdigit():
                return float(valore)
        return False
    
    def valida_date(valore: str):
        # Regex YYYY/MM/DD
        pattern = r"^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"
        if re.match(pattern, valore):
            return valore
        return False
    
    # def valida_auto_increment() -> int:
    #     current_tab = db[nome_db].get(nome_tab, [])
    #     if not current_tab:
    #         return 1
    #     latest_id = current_tab[-1][0]
    #     return latest_id + 1
        
    
    def valida_input(valore, tipo):
        mappa_validatori = {
            "char": valida_char,
            "int": valida_int,
            "bool": valida_bool,
            "double": valida_double,
            "date": valida_date,
            # "update": valida_auto_increment
        }
        funzione = mappa_validatori.get(tipo)
        if funzione:
            return funzione(valore)# costruzione della funzione da usare 
        return False
    
    match crud:
        case "create":
            load_user = user.split("-")
            nomi_colonne = list(schema_tab.keys()) # ["nome", "prezzo"]
            tipi_colonne = list(schema_tab.values()) # ["char", "double"]
            dati_validati = []
            
            if len(load_user) == len(nomi_colonne):
                for i in range(len(load_user)):
                    da_validare = load_user[i].strip()
                    tipo_atteso = tipi_colonne[i]
                    nome_colonna = nomi_colonne[i]
                    result = valida_input(da_validare, tipo_atteso)
                    
                    if result is not False and result != "not_bool":
                        dati_validati.append(result)
                        print(f"\n Colonna {nome_colonna}: '{da_validare}' VALIDATO come {tipo_atteso} ")
                    else:
                        print(f"\n Errore: '{da_validare}' non è un {tipo_atteso} valido per '{nome_colonna}'\n ")
                        return False
                return dati_validati
            else:
                print(f"Errore: Numero di campi errato. Attesi {len(nomi_colonne)}, ricevuti {len(load_user)}")
                return False
            
        case "update":
            if user != "" and "->" in user :
                user = user.strip()
                parti = user.split("->")
                # parti = [p.strip() for p in user.split("->")]
                print("DEBUG: parti", parti)
                part_0 = parti[0].strip()
                part_1 = parti[1].strip()
                print(f"DEBUG: part_0 '{part_0}'  ")
                print(f"DEBUG: part_1 '{part_1}'  ")
            else:
                print("ERRORE: update non nel formato richiesto ('old -> new')\n" )
                return False
            
            if len(parti) == 2 and part_0 != part_1:
                nomi_colonne = list(schema_tab.keys()) # ["nome", "prezzo"]
                tipi_colonne = list(schema_tab.values()) # ["char", "double"]
                dati_validati = []
                old_param = part_0
                da_validare = part_1
                row = db[nome_db][nome_tab][id_row]
                print("DEBUG: rew:", row)
                # tipo_atteso = tipi_colonne[old_param]
                idx_tomatch = -1
                for i, valore_db in enumerate(row):
                    if str(valore_db) == old_param: # Confronto tra stringhe
                        idx_tomatch = i
                        break
            
                if idx_tomatch != -1:
                    print(f"DEBUG: Found '{old_param}' at index: {idx_tomatch}")
                    tipo_atteso = tipi_colonne[idx_tomatch]
                    nome_colonna = nomi_colonne[idx_tomatch]
                            
                    result = valida_input(da_validare, tipo_atteso)
                    print(f"DEBUG: result '{result}' typo: {type(result)}")
                    
                    if result is not False and result != "not_bool":
                        dati_validati.append(result)
                        print(f"VALIDATO: {nome_colonna} -> {result} come {tipo_atteso}")
                        return dati_validati , row, old_param, idx_tomatch
                    else:
                        print(f"\n Errore: '{da_validare}' non è un {tipo_atteso} valido per '{nome_colonna}'\n ")
                        return False
                else:
                    print(f"ERRORE: dato non trovato nel record {row}")
                    return False
                
        case _ :
            exit()
                       
@log_func
def popola():
    
    def add(nome_tab: str, record: list):
        if record in db[nome_db][nome_tab]:
            print(f"ERRORE: Il record {record} è già presente nel database!")
            return False
        else:
            db[nome_db][nome_tab].append(record)
            # print(f"DEBUG: {db}")
            print(f"\n SUCCESSO! Record aggiunto a {nome_db} -> {nome_tab}\n ")
            return True
    
    def drop(nome_tab: str, record: list, id_row: int, mode: str):
        match mode:
            
            case "one":
                if record in db[nome_db][nome_tab]:
                    eliminato = db[nome_db][nome_tab].pop(id_row)
                    print(f"SUCCESSO: Rimosso Il record {eliminato}.")
                    return True
                else:
                    print("Errore: ID non trovato.")
                    return False
                
            case "all":
                if nome_tab in db[nome_db]:
                    eliminata = db[nome_db][nome_tab].clear() #.pop()cancella tutto l'ogetto
                    # schema_tabelle[nome_tab].clear()
                    print(f"SUCCESSO: Rimossa Tabella: {nome_tab, eliminata}.")
                    return True
                else:
                    print("Errore: Tabella non trovata.")
                    return False
                
    def fix(nome_tab:str , record:list, id_row:int, mode: str,):
        # return dati_validati , row, old_param, idx_tomatch (return di def valida)
        print(f"DEBUG: record[2] '{record[2]}' ")
        print(f"typo of record[2] {type(record[2])}")
        print(f"fi record in :  {db[nome_db][nome_tab][id_row]}")
        print(f"mode: {mode}")
        if record[2] in db[nome_db][nome_tab][id_row]:
            match mode:
                
                case "whole":
                    pass
                
                case "one":
                    to_add = record[0]# il parametro da andare a switchare
                    row = record[1]# tutta la riga da andare ad iterare
                    old_param = record[2]# il parametro da droppare
                    idx_list = record[3]
                    print(f"DEBUG: to_add:{to_add}, row:{row}, old_param:{old_param}, idx_list:{idx_list}")
                    
                    if old_param in row:
                        db_row = db[nome_db][nome_tab][id_row][idx_list]
                        db_row[old_param] = db_row[to_add]
                        print(f"SUCCESSO: fix di {old_param} -> {to_add}")
                        return True
                        
                        
                    
                    
                    
                    #TODO: già tutto validato devo solo prendere il vecchio e sostituirlo con il nuovo 
                    pass
        else:
            print("ERRORE: Record non esistente")
        #TODO: finzione per l'update 
            

    print(f"\n --- AVVIO MODALITA POPOLAMENTO ---\n")
    global db
    
    while True:
        nome_tab = input(f"\nQuale tabella vuoi popolare? Tabelle: {schema_tabelle.keys()} :").lower()
        if nome_tab in schema_tabelle.keys() and nome_tab in db[nome_db]:
            nome_tab = nome_tab
            break
        else:
            print("Tabella non Esistente! ")
            continue #Torna a chiedere nome_tab
    
    if not schema_tabelle.get(nome_tab):
        print("tabella senza colonne")
        return
    else:
        schema_tab = schema_tabelle.get(nome_tab)
        
    while True:
        if "popola" in scelte:
            print(logged_user)
            
            while True:
                update_scelte("logged_lv3")
                
                #["create", "read", "update", "delete", "back"]
                crud = input(f"\n Scegli l'azione che vuoi fare in {nome_tab}: {scelte}: ").lower()
                
                if crud == "back":
                    update_scelte("logged_lv2")
                    break #Esce da crud
                
                if not crud in scelte:
                    print("non è una crud ")
                    continue
                else:
                    match crud:
                        
                        # -- CREATE 1---
                        case "create":
                            print("\n--- FASE : CREATE ---\n")
                            
                            while True:
                                print(f"La tabella '{nome_tab}' ha il seguente schema colone: {schema_tab}")
                                insert = input(f"Popola {nome_tab}' seguendo lo schema, separando i valori con il simbolo ( - ) o 'back': ")
                                if insert.lower() == "back":
                                    break
                                
                                record = valida(crud, insert, schema_tab) #return dati_vliati [] o false
                                
                                if record:
                                    if add(nome_tab, record): 
                                        
                                        if input("Vuoi inserire un altro record? (y/n): ").lower() != "y":
                                            break    
                                else:
                                    # Se record è false, il messaggio di errore è già stampato da valida()
                                    print("Riprova l'inserimento o scrivi 'back'.\n")
                                        
                        # -- READ ALL---           
                        case "read":
                            print(f"\n--- FASE : READ - TABELLA: {nome_tab} ---\n")
                            view_tab(nome_tab, schema_tab)
                        
                        # -- UPDATE 1---
                        case "update":
                            print(f"\n--- FASE : UPDATE - TABELLA: {nome_tab} ---\n")
                            
                            while True:
                                view_tab(nome_tab, schema_tab)
                                id_row = input("Scegli 'back' o l'ID della riga da modificare: ").strip()
                                
                                if id_row == 'back':
                                    break
                                elif id_row.isdigit():
                                    id_row = int(id_row)
                                else:
                                    print("ERRORE: id_row deve essere uno tra i numeri che vedi")
                                    continue
                                
                                if id_row > len(db[nome_db][nome_tab]):
                                    print(f"\nERRORE: id_row {id_row} NON esiste!\n")
                                    continue
                                
                                else:                                    
                                    row_tofix = db[nome_db][nome_tab][id_row]
                                    print("DEBUG:", row_tofix, "DB:", db)
                                    scelta = input(" scegli 'back' o tra modificare ['whole', 'one']").lower()
                                    
                                    if not scelta in ('whole', 'one'):
                                        print("ERRORE: scelta non valida")
                                        continue
                                    elif scelta == "back":
                                        break
                                    
                                    print(f"\nLa tabella '{nome_tab}' ha il seguente schema colone: {schema_tab}")
                                    print(f"La row da fixare: {row_tofix}\n")
                                    # --- WHOLE ---
                                    if scelta == "whole":
                                        pass 
                                    
                                    # --- ONE ---
                                    elif scelta == "one":
                                        user = input("modifica così: (parametro -> parametro modificato): ").lower()
                                        
                                        record = valida(crud, user, schema_tab, nome_tab, id_row)
                                        
                                        if record != False:
                                            if fix(nome_tab, record, id_row, mode=scelta):
                                                
                                                if input("Vuoi modificare un altro record? (y/n): ").lower() != "y":
                                                    break    
                                        else:
                                            # Se record è false, il messaggio di errore è già stampato da valida()
                                            print("Riprova l'inserimento o scrivi 'back'.\n")
                                            continue                                    
                                    
                                    # TODO:continuare, valutare se logica a modifica sincolo parametro o tutta la stringa  
                            
                        # -- DELETE ---    
                        case "delete":
                            print(f"\n--- FASE : DELETE - TABELLA: {nome_tab} ---\n")
                            
                            while True:
                                user = input("scegli 'back' o tra elimina ['all', 'one']: ").lower()
                                if not user in ('all', 'one', 'back'):
                                    print("ERRORE: non è una scelta disponibile")
                                    continue
                                elif user == "back":
                                    break
                                
                                # -- DELETE 1--- 
                                elif user == "one":
                                    while True:
                                        print("\n")
                                        view_tab(nome_tab, schema_tab)
                                        
                                        id_row = input("Scegli 'back' o l'ID della riga da cancellare: ").strip()
                                        
                                        if id_row == 'back':
                                            break
                                        elif id_row.isdigit():
                                            id_row = int(id_row)
                                        else:
                                            print("\nERRORE: id_row deve essere uno tra i numeri che vedi\n")
                                            continue
                                        
                                        if id_row >= len(db[nome_db][nome_tab]):
                                            print(f"\nERRORE: id_row {id_row} NON esiste!\n")
                                            continue
                                        else:                                            
                                            record = db[nome_db][nome_tab][id_row]
                                            if input(f"Vuoi davvero eliminare {record}? (y/n): ").lower() != "y":
                                                break
                                            
                                            if not drop(nome_tab, record, id_row, user):
                                                print("\nERRORE: riga NON cancellata\n")
                                                continue
                                            else:
                                                
                                                if input("\nvuoi ELIMINARE un alto record? (y/n): ").lower() != "y":
                                                    break
                                                
                                # -- DELETE ALL---               
                                elif user == "all":
                                    while True:
                                        print("\n")
                                        view_tab(nome_tab, schema_tab)
                                        
                                        if input(f"sei proprio sicuro di ELIMINARE tabella: '{nome_tab}'? (y/n): ") != "y":
                                            break
                                        else: 
                                            del_tab = input("\nInserisci il nome esatto della tabella per procedere: ").lower()
                                            
                                            if del_tab != nome_tab:
                                                print("ERRORE: nome tabella errato")
                                                break
                                            
                                            else:
                                                if not drop(nome_tab, record=[], id_row=0, mode=user):
                                                    print("\nERRORE: tabella NON cancellata\n")
                                                    continue
                                                else:
                                                    # if input("\nvuoi ELIMINARE un altra tabella? (y/n): ").lower() != "y": 
                                                    # TODO: gestire questa situazione, rompe perche cancellando la tabella scelta non la ritrova
                                                    # prova?: chiedere nuovamente dentro dal all il nome_tab da eliminare
                                            
                                                        break                  
            print("DEBUG: USCITA")    
            break #Esce da while 1
        
        update_scelte("logged_lv2")
    
           
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def play():
    login()
    
    while True:
        update_scelte("")
        print("STATO: ", logged_user)
        user = input(f"\ncosa vuoi fare? : {scelte} (").lower()
        
        if user in scelte:
            
            match user:
                case "exit":
                    exit()
                
                case "back":
                    #TODO: se back torna a login, resetta nome_db e (NUOV: seleziona_db) 
                    # opzione che appare al login, solo se un db è stato creato in precedenza
                    # capire dove salvare i db creati. 
                    # seleziona_db aggiorna global nome_db e carica le tabelle(schema_tab e db{})
                    pass
                
                case "crea_new_user":
                    registra_utente()
                    
                case "crea_db":
                    crea_db()
                    
                case "crea_tab":
                    crea_tab()
                
                case "crea_col":
                    nome_tab = input(f"In quale tabella vuoi inserire la nuova colonna? Tabelle: {schema_tabelle.keys()} :").lower()
                    if nome_tab in schema_tabelle.keys():
                        crea_col(nome_tab)
                    else:
                        print("ERRORE")
                        
                case "popola":
                    popola()                    
                case _:
                    print(f"Errore: '{user}' non è tra le scelte disponibili: {scelte}")
                    continue
                    
play()