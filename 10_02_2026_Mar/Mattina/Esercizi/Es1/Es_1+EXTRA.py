import datetime

# Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

# __ CLASSE USR ---
class User:
    def __init__(self, nome: str, password):
        self.nome = nome
        self.password = password
        self. magazzini_posseduti = []

    def __str__(self):
        return f"UTENTE: {self.nome}"
    
    @log_func
    def crea_magazzino(self, nome_magazzino):
        nuovo_id = len(self.magazzini_posseduti) + 1
        magazzino_OBJ = Magazzino(nome_magazzino, id=nuovo_id)
        self.magazzini_posseduti.append(magazzino_OBJ)
        print(f"Magazzino {nome_magazzino} creato con successo.")
        return magazzino_OBJ
    
    @log_func
    def elimina_magazzino(self, nome_magazzino):
        if nome_magazzino in self.magazzini_posseduti:
            magazzino_da_eliminare = self.magazzini_posseduti[nome_magazzino]
            while True:
                conferma = input(f"vuoi davvero eliminare {nome_magazzino} ? (y/n)").lower().strip()
                if conferma != "y":
                    break
                else: 
                    if input(f"scrivi il nome del magazzino che vuoi eliminare: ") == magazzino_da_eliminare:
                        self.magazzini_posseduti.pop(nome_magazzino)
                        print(f"Magazzino {nome_magazzino} ELIMINATO con succsso!")
                        break
                
    def stampa_magazzini_posseduti(self):
        print(f"--- MAGAZZINI DI {self.nome.capitalize()} ---")
        if not self.magazzini_posseduti:
            print("Non hai ancora magazzini, Creane 1.")
        else:
            print(self.magazzini_posseduti)
        print("----------------------------------")
            

# --- CLASSE PACCO  ---
class Pacco:
    stati_possibili = {"in magazzino", "in consegna", "consegnato"}
    
    def __init__(self, codice: str, peso: float):
        self.codice = codice
        self.peso = peso
        self.stato = "in magazzino"

    def __str__(self):
        return f"PACCO: '{self.codice}' | Peso: {self.peso}kg | Stato: {self.stato}"
    
    @log_func
    def cambia_stato(self, new_stato: str):
        if new_stato in self.stati_possibili:
            self.stato = new_stato
            print(f"   >>> Stato di {self.codice} aggiornato a: {self.stato}")
            return True
        else:
            print(f"   >>> ERRORE: Stato '{new_stato}' non valido!")
            return False

# --- CLASSE MAGAZZINO  ---
class Magazzino:
    def __init__(self, nome, id):
        self.nome = nome
        self.inventario = {} # Dict: "codice" -> Oggetto Pacco

    def stampa_inventario(self):
        print(f"--- INVENTARIO DI {self.nome.lower()} ---")
        if not self.inventario:
            print("Il magazzino è vuoto.")
        else:
            # Iteriamo sui valori (gli oggetti Pacco)
            for p in self.inventario.values():
                print(p) #__str__ di Pacco
        print("----------------------------------")
            
    @log_func   
    def aggiungi_pacco(self, codice: str, peso: float):
        codice = codice.lower()
        if codice not in self.inventario:
            nuovo_pacco_OBJ = Pacco(codice, peso)
            self.inventario[codice] = nuovo_pacco_OBJ
            print(f"Pacco '{codice}' inserito.")
            return nuovo_pacco_OBJ
        else:
            print(f"Errore: Pacco '{codice}' già esistente.")
            return None
    
    @log_func
    def rimuovi_pacco(self, codice: str):
        codice = codice.lower()
        if codice in self.inventario:
            del self.inventario[codice]
            print(f"Pacco '{codice}' rimosso dal sistema.")
        else:
            print(f"Errore: '{codice}' non trovato.")
    
    @log_func
    def get_pacco_o_lista(self, ricerca):
        """Cerca un pacco singolo per codice OPPURE una lista per stato."""
        ricerca = ricerca.lower()
        
        # per STATO 
        if ricerca in Pacco.stati_possibili:
            pacchi_trovati = []
            for p in self.inventario.values():
                if p.stato == ricerca:
                    pacchi_trovati.append(p)
            print(f"Trovati {len(pacchi_trovati)} pacchi in stato '{ricerca}'")
            return pacchi_trovati
        
        # per CODICE 
        elif ricerca in self.inventario:
            pacco = self.inventario[ricerca]
            print(f"Pacco trovato: {pacco.codice}")
            return pacco
            
        else:
            print("Nessun risultato trovato.")
            return None

# --- CLASSE GESTORE ---
class GestorePacchi:
    
    def __init__(self, magazzino_riferimento, utente):
        self.magazzino = magazzino_riferimento
        self.utenti_registrati = [utente]

    @log_func
    def metti_in_consegna(self, codice_pacco):
        pacco = self.magazzino.get_pacco_o_lista(codice_pacco)
        
        if isinstance(pacco, Pacco):
            pacco.cambia_stato("in consegna")
        else:
            print("ERRORE: Operazione annullata: pacco non valido.")

    @log_func
    def segna_consegnato(self, codice_pacco):
        pacco = self.magazzino.get_pacco_o_lista(codice_pacco)
        
        if isinstance(pacco, Pacco):
            pacco.cambia_stato("consegnato")
        else:
            print("ERRORE: Operazione annullata: pacco non valido.")

    @log_func
    def calcola_peso_da_consegnare(self):
        totale_peso = 0
        conta_pacchi = 0
        
        for p in self.magazzino.inventario.values():
            if p.stato != "consegnato":
                totale_peso += p.peso
                conta_pacchi += 1
                
        print(f"STATISTICHE: Ci sono {conta_pacchi} pacchi ancora da smaltire.")
        print(f"PESO TOTALE RIMANENTE: {totale_peso} kg")
        return totale_peso
    
    
    

def play():
    print("\n--- BENVENUTO NEL SISTEMA LOGISTICO ---")
    
    # Istanziamento classi
    # utenti = [] #TODO: questo va nella classe Gestore perche voglio che Gestore Pacchi sia la classe che rappresenta l'hub app
    # magazzini = [  ] #TODO: questo va nella classe User
    
    first_user_OBJ = User("marco","M13K")
    my_magazzino_OBJ = Magazzino("mio")
    my_gestore_OBJ = GestorePacchi(my_magazzino_OBJ)
    first_user_OBJ.append(my_magazzino_OBJ.nome)
    
    # --- LOGICA LOGIN --_
    while True:
        user_name = input("inserisci il tuo nome utente")
        user_pass = input("inserisci la tua password")
        break #TODO: da finire 
    
    while True:
        nome_hub = input("Inserisci il nome del Magazzino: ")
        
        if not nome_hub in magazzini:
            print("ERRORE: Magazzi non trovato!")
            
            if not input("Vuoi Riprovare? (y/n)").lower() == "y":
                break
            else:
                continue
        else:
            break
           
                
    
    # print("\n[Init] Caricamento dati del magazino...")
    # my_magazzino_OBJ.aggiungi_pacco("TEST-01", 1.5)
    # my_magazzino_OBJ.aggiungi_pacco("TEST-02", 4.5)
    # my_magazzino_OBJ.aggiungi_pacco("TEST-03", 1.5)
    # my_magazzino_OBJ.aggiungi_pacco("TEST-04", 5.0)
    # my_magazzino_OBJ.aggiungi_pacco("TEST-05", 1.5)

    while True:
        print(f"\n--- MENU OPERATIVO: {my_magazzino_OBJ.nome.lower()} ---")
        print("1)  [Magazzino] Aggiungi nuovo Pacco")
        print("2)  [Magazzino] Stampa Inventario")
        print("3)  [Magazzino] Cerca (Codice o Stato)")
        print("4)  [Magazzino] Rimuovi Pacco")
        print("-" * 30)
        print("5)  [Gestore] Metti in Consegna")
        print("6)  [Gestore] Segna come Consegnato")
        print("7)   [Gestore] Calcola Peso Rimanente")
        print("-" * 30)
        print("0) Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        # --- LOGICA MAGAZZINO ---
        if scelta == "1":
            cod = input("Codice Pacco: ")
            try:
                peso = float(input("Peso (kg): "))
                my_magazzino_OBJ.aggiungi_pacco(cod, peso)
            except ValueError:
                print("ERRORE: Il peso deve essere un numero (usa il punto per i decimali).")

        elif scelta == "2":
            my_magazzino_OBJ.stampa_inventario()

        elif scelta == "3":
            query = input("Cosa cerchi? (Inserisci Codice univoco o Stato): ")
            # gegestisce entrambi i casi
            my_magazzino_OBJ.get_pacco_o_lista(query)

        elif scelta == "4":
            cod = input("Codice pacco da rimuovere: ")
            my_magazzino_OBJ.rimuovi_pacco(cod)

        # --- LOGICA GESTORE ---
        elif scelta == "5":
            cod = input("Inserisci codice pacco da spedire: ")
            my_gestore_OBJ.metti_in_consegna(cod)

        elif scelta == "6":
            cod = input("Inserisci codice pacco consegnato: ")
            my_gestore_OBJ.segna_consegnato(cod)

        elif scelta == "7":
            my_gestore_OBJ.calcola_peso_da_consegnare()

        # --- USCITA ---
        elif scelta == "0":
            print(" Ciao!")
            break
        
        else:
            print(" Scelta non valida, riprova.")


play()