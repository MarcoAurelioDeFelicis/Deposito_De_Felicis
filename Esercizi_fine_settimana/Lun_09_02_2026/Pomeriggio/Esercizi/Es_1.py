# Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, 
# gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. 
# Il sistema sarà strutturato in tre parti principali:

# Gestione Clienti:
# I clienti possono visualizzare gli articoli disponibili in inventario.
# I clienti possono selezionare e acquistare articoli dall'inventario.
# Il sistema tiene traccia degli acquisti dei clienti.

# Gestione dell'Inventario:
# Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
# È possibile aggiungere nuovi articoli all'inventario.
# Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).

# Amministrazione:
# l'analisi del negozio da parte degli amministratori.
# Gli amministratori possono visualizzare lo stato corrente dell'inventario.
# Il sistema tiene traccia dei guadagni totali.
# Puoi pre inserire gli amministratori non i clienti

# Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione, 
# nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori.
import datetime

class User:
    def __init__(self, nome: str, password, id_assegnato, tipo: str):
        self.nome = nome
        self.password = password
        self.tipo = tipo
        self.isadmin = False
        self.id = id_assegnato

    def __str__(self):
        ruolo = "ADMIN" if self.isadmin else "USER"
        return f"ID: {self.id:<3} | UTENTE: {self.nome:10} | RUOLO: {ruolo}"

    def promuovi_a_admin(self, esecutore):
        """Cambia lo stato a admin solo se l'esecutore ha i permessi."""
        if esecutore.isadmin:
            self.isadmin = True
            return True
        return False
                
        
        
class Magazzino():
    def __init__(self, nome):
        self.nome = nome
        self.aperto = False
        self.inventario = {}
        self.incasso = 0.0
        self.ordini = []
    #4    
    def stampa_inventario(self):
        print(f"\n--- INVENTARIO DI {self.nome.upper()} ---")
        if not self.inventario:
            print("Il menu è vuoto.")
        else:
            for p in self.inventario:
                # Recuperiamo i dati usando la chiave 'p'
                dati = self.inventario[p] 
                # Stampiamo nome, prezzo e quantità
                print(f"- {p}: €{dati['prezzo']} (Disponibili: {dati['quantita']})")
        print("--------------------------\n")
    #5    
    def aggiungi_articolo(self, nome, prezzo, quantita):
        nome = nome.capitalize()
        if nome in self.inventario:
            self.inventario[nome]['quantita'] += quantita
            #TODO: se quantità 0 lo rimuove da magazino
            print(f"Aggiornata scorta di {nome}. Nuova quantità: {self.inventario[nome]['quantita']}")
        else:
            self.inventario[nome] = {'prezzo': prezzo, 'quantita': quantita}
            print(f"Articolo '{nome}' inserito correttamente.")
    #6
    def rimuovi_articolo(self, nome):
        nome = nome.capitalize()
        if nome in self.inventario:
            del self.inventario[nome]
            print(f"Articolo '{nome}' rimosso dal sistema.")
        else:
            print(f"Errore: '{nome}' non trovato in inventario.")
    #7
    def aggiorna_articolo(self, nome, nuovo_prezzo=None, nuova_quantita=None):
        nome = nome.capitalize()
        if nome in self.inventario:
            if nuovo_prezzo is not None:
                self.inventario[nome]['prezzo'] = nuovo_prezzo
            if nuova_quantita is not None:
                self.inventario[nome]['quantita'] = nuova_quantita
            print(f"Dati di '{nome}' aggiornati con successo.")
        else:
            print(f"Errore: Impossibile aggiornare, '{nome}' non esiste.")
    #8       
    def crea_ordine(self, nome_articolo, quantita_richiesta, cliente):
        nome = nome_articolo.capitalize()
        
        if nome not in self.inventario:
            print(f"ERRORe: '{nome}' non è a listino.")
            return False
        
        articolo = self.inventario[nome]
        
        #controllo disponibilità
        if articolo['quantita'] < quantita_richiesta:
            print(f"ERRORe: Disponibilità insufficiente (Solo {articolo['quantita']} pezzi).")
            return False
        
        # calcolo costi e aggiornamento
        prezzo_unitario = articolo['prezzo']
        totale_ordine = prezzo_unitario * quantita_richiesta
        
        # scalo dall'inventario e aggiunt all'incasso
        articolo['quantita'] -= quantita_richiesta
        self.incasso += totale_ordine
        
        # salvataggio ordine
        nuovo_ordine = {
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
            "cliente": cliente,
            "articolo": nome,
            "quantita": quantita_richiesta,
            "totale": totale_ordine
        }
        self.ordini.append(nuovo_ordine)
        
        print(f"Ordine completato! {quantita_richiesta}x {nome} per €{totale_ordine:.2f}")
        return True
    #9
    def stampa_ordini(self):
        print(f"\n---  STORICO ORDINI: {self.nome.upper()} ---")
        if not self.ordini:
            print("Nessun ordine registrato.")
        else:
            for i, o in enumerate(self.ordini, 1):
                print(f"{i}. [{o['data']}] {o['cliente']:10} ha comprato {o['quantita']}x {o['articolo']} (Tot: €{o['totale']:.2f})")
        print("------------------------------------------\n")
        
        
def login(user_name: str, password: str, utenti):
        user = utenti.get(user_name.lower())
        # se l'utente esiste e la password coincide
        if user and user.password == password:
            print(f"\n--- SESSIONE ATTIVA: {user.nome} ({'ADMIN' if user.isadmin else 'USER'}) ---")
            return user
        else:
            print("\nCredenziali errate!")
            return None
        
# --- TESRT --- 
def play():
    utenti = {}
    deposito = Magazzino("Magazzino Centrale")
    
    # creazione Admin iniziale 
    root = User("marco", "M123K", 1, "boss")
    root.isadmin = True
    utenti[root.nome] = root
    
    current_user = None
    
    while True:
        scelta_iniziale = input("Chi sei ? ('cliente' o 'staff')? ")
        if not scelta_iniziale in ('cliente','staff'):
            print("ERRORE: scelta non possibile")
            continue            
        
        #--- LOGIN ---
        if scelta_iniziale == 'staff':
            while True:
                
                print("FASE: LOGIN\n")
                
                name = input("User Name: ").lower()
                password = input("Password: ")
                        
                current_user= login(name, password, utenti)
                print("--------------------------\n")
                    
                if current_user:
                    break
                else:
                    print("ERRORE: Login fallito. Riprova.")
                    print("usa '<-' per uscire!!!!\n")
                    continue
        else:
            while True:
                name = input("Come ti chiami?: ").lower()
                
                if not name.isdigit():
                    current_user = User(name, "null", 999, 'cliente')
                    print(f"\n--- SESSIONE ATTIVA: {current_user.nome} ---")
                    break
                
                else:
                    print("ERRORE: nome utente non valido, Riprova")
                    continue
                
        
        print(f"DEBUG: current user:{current_user}")
        # print("DEBUG: Inizial di User sato ") 
        
        #Inizial di User sato
        state_admin = False 
        
        if current_user.isadmin == True:
            state_admin = True
        else:
            state_admin = False
            
        while True:
            scelte_disponibili = ["0"] 
                    
            # Gestione permessi e menu
            if state_admin:
                scelte_disponibili.extend(["1", "2", "3", "4", "9"]) # Admin vede utenti e log
                print("\nMENU ADMIN:")
                print("1) Visualizza Utenti") #TODO : aggiungere funzione in user
                print("2) Crea Nuovo Utente") #TODO : aggiungere funzione in user BUG: deve bloccare l'aggiunta di un utente gia inserito
                print("3) Promuovi Utente")
                print("4) Visualizza Inventario")
                print("9) Visualizza Storico Ordini")
            elif current_user.tipo == 'staff':
                scelte_disponibili.extend(["4", "5", "6", "7", "9"])
                print("\nMENU STAFF:")
                print("4) Visualizza Inventario")
                print("5) Aggiungi/Rifornisci Articolo")
                print("6) Rimuovi Articolo")
                print("7) Aggiorna Prezzo/Quantità")
                print("9) Visualizza Storico Ordini")
            else: # Cliente
                scelte_disponibili.extend(["4", "8"])
                print("\nMENU CLIENTE:")
                print("4) Visualizza Prodotti")
                print("8) Acquista Prodotto (Ordina)")
                
            print("0) Esci")
            
            opzione = input("\nScegli opzione: ")
            
            if opzione not in scelte_disponibili:
                print("ERRORE: Scelta non disponibile o permessi insufficienti.\n")
                continue
            
            # --- LOGICA AZIONI ---
            else:
                # 1, 2, 3: Gestione Utenti
                if opzione == "1":
                    print("\nDATABASE UTENTI:")
                    for u in utenti.values():
                        print(u)
                    print("--------------------------\n")

                elif opzione == "2":
                    print("\nFASE: CREA NEW USER \n")
                    nome = input("Nome nuovo utente: ")
                    pw = input("Password: ")
                    nuovo_id = len(utenti) + 1
                    
                    user_OBJ = User(nome, pw, nuovo_id, "staff")
                    utenti[nome.lower()] = user_OBJ
                    print(f"Utente {nome} creato con successo.")

                elif opzione == "3":
                    id_target = input("ID utente da promuovere: ")
                    for u in utenti.values():
                        if str(u.id) == id_target:
                            u.promuovi_a_admin(current_user)
                            print(f"{u.nome} promosso!")
                        else:
                            print(f"ERRORE: {id_target} non trovato ")
                            
                # 4 stampa solo magazzino
                elif opzione == "4":
                    deposito.stampa_inventario()
                
                # 5, 6, 7: Gestione Magazzino (Staff/Admin)
                elif opzione == "5":
                    nome = input("Nome articolo: ")
                    try:
                        prezzo = float(input("Prezzo: "))
                        qta = int(input("Quantità: "))
                        deposito.aggiungi_articolo(nome, prezzo, qta)
                    except ValueError: print("Errore: inserire numeri validi.")

                elif opzione == "6":
                    nome = input("Nome articolo da rimuovere: ")
                    deposito.rimuovi_articolo(nome)

                elif opzione == "7":
                    nome = input("Nome articolo da modificare: ")
                    p_inp = input("Nuovo prezzo (premi invio per non cambiare): ")
                    q_inp = input("Nuova quantità (premi invio per non cambiare): ")
                    p = float(p_inp) if p_inp else None
                    q = int(q_inp) if q_inp else None
                    deposito.aggiorna_articolo(nome, p, q)
                    
                # 8 Ordine (Cliente)
                elif opzione == "8":
                    prod = input("Cosa vuoi acquistare? ")
                    try:
                        qta = int(input("Quantità: "))
                        deposito.crea_ordine(prod, qta, current_user.nome)
                    except ValueError: print("Errore: inserire un numero intero.")
                    
                # 9 Storico (Staff/Admin)
                elif opzione == "9":
                    deposito.stampa_ordini()

                elif opzione == "0":
                    break

play()