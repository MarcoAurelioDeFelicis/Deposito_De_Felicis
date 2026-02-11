# Classe Prodotto:
# Attributi:
# nome (stringa che descrive il nome del prodotto)
# costo_produzione (costo per produrre il prodotto)
# prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
# Metodi:
# calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
# Classi parallele:
# Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
# Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
# Classe Fabbrica:
# Attributi:
# inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
# Metodi:
# aggiungi_prodotto: aggiunge prodotti all'inventario.
# vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
# resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.
# Decoratore

import inspect
import random
from functools import wraps

#Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

# --- CLASSE PRODOTTO  ---
class Prodotto:
    def __init__(self, nome: str, costo_produzione: float, prezzo_vendita: float, unita: int, categoria:str):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.unita = unita
        self.categoria = categoria
        
    def calcola_profitto(self, quantita_da_vendere):
        profitto = self.prezzo_vendita * quantita_da_vendere - self.costo_produzione * quantita_da_vendere
        print(f"profitto prodotto: {profitto}\n")
        print(f"costo di produzione * unita {self.costo_produzione * quantita_da_vendere}")
        return profitto 
    
    def __str__(self):
        return f"PRODOTTO: '{self.nome}' | Prezzo: {self.prezzo_vendita}$ | Unità: {self.unita}"

# --- CLASSE ELETTRONICA(Prodotto) ---
class Elettronica(Prodotto):
    def __init__(self, nome: str, costo_produzione: float, prezzo_vendita: float, unita:int, categoria: str, componenti: dict, classe_energetica: str):
        super().__init__(nome, costo_produzione, prezzo_vendita, unita, categoria)
        self.componenti = componenti
        self.classe_energetica = classe_energetica
        
    def __str__(self):
        return f"(Categoria: {self.categoria}) " + super().__str__() 

# --- CLASSE ABBIGLIAMENTO(Prodotto) ---
class Abbigliamento(Prodotto):    
    
    taglie_disponibili = ("XL","L","M","S","XS" )
    
    def __init__(self, nome: str, costo_produzione: float, prezzo_vendita: float, unita: int, categoria: str, materiale: str, taglia:str):
        super().__init__(nome, costo_produzione, prezzo_vendita, unita, categoria)
        self.materiale = materiale
        self.taglia = taglia
        
    def __str__(self):
        return f"(Categoria: {self.categoria}) " + super().__str__() 
        

# --- CLASSE FABBRICA ---
class Fabbrica:
    TIPI_PROD = {"elettronica": Elettronica, "abbigliamento": Abbigliamento}
    
    def __init__(self, nome, inventario=None):
        self.inventario = inventario if inventario is not None else {}
        self.storico_vendite = {}
        self.nome = nome
        
#-------------- METODI FABBRICA --------------------------------------------
        
    def stampa_inventario(self):
        print(f"--- INVENTARIO DI: {self.nome.lower()} ---")
        if not self.inventario:
            print("Il magazzino è vuoto.")
            return None
        else:
            # Iteriamo sui valori (gli oggetti Pacco)
            for p in self.inventario.values():
                print(p) #__str__ di Pacco
        print("----------------------------------")
        return True
    
    @staticmethod   
    def zero_checker(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            #Run del metodo wrappato
            result = func(self, *args, **kwargs)
            if hasattr(self, 'inventario'):
                self.inventario = {k: v for k, v in self.inventario.items() if v.unita > 0}
            
                # for k, v in self.inventario:
                #     if v.unita <= 0: 
                #         del self.inventario[k]
            
            return result
        return wrapper
            
    def asker(self, categoria: str):
        ''' Trova i parametri necessari e chiede l'input all'utente '''
        if categoria.lower() == 'back':
            return None
        
        classe_scelta = self.TIPI_PROD.get(categoria)
                
        #firma del metodo __init__
        parametri = inspect.signature(classe_scelta.__init__).parameters
        
        args_da_passare = []
        
        print(f"\n--- Configurazione prodotto {classe_scelta.__name__} ---")
        for nome_param, param in parametri.items():
            # Skip 'self'
            if nome_param == 'self': continue
            
            valore_input = input(f"Inserisci {nome_param}: ")
            #default str perche input è gia str
            tipo_atteso = param.annotation if param.annotation != inspect.Parameter.empty else str
            
            try:
                valore_convertito = tipo_atteso(valore_input)
                args_da_passare.append(valore_convertito)
            except ValueError:
                print(f"ERRORE: '{valore_input}' non è un valore valido per {tipo_atteso.__name__}.")
                return None
                # args_da_passare.append(valore_input) 
                    
        return args_da_passare
    
    @log_func
    @zero_checker
    def crea_prodotto(self, classe_scelta, args_lista):
        ''' Spacchetta * gli argomenti e istanzia OBJ della classe '''
        
        try:
            new_OBJ = classe_scelta(*args_lista)
            return new_OBJ
        
        except Exception as e:
            print(f"ERRORE: durante la creazione: {e}")
            return None


    @log_func   
    def aggiungi_prodotto(self, prodotto: Prodotto):
        
        #crea_prodotto()
        prodotto_OBJ = prodotto
        if not prodotto_OBJ.nome in self.inventario:
            self.inventario[prodotto_OBJ.nome] = prodotto_OBJ
            print(f"prodotto {prodotto_OBJ.nome} aggiunto all'inventrio\n")
            print(f"Inventario AGGIORNATO :")
            
            self.stampa_inventario()
        else:
            print("ERRORE")
            
    @log_func 
    @zero_checker       
    def vendi_prodotto(self, nome_prodotto: str, quantita_da_vendere: int):
        # prodotto_OBJ = [i for i in self.inventario if i == nome_prodotto]
        prodotto_OBJ = self.inventario.get(nome_prodotto)
    
        if prodotto_OBJ and quantita_da_vendere <= prodotto_OBJ.unita:
            prodotto_OBJ.unita -= quantita_da_vendere
            cod_tracciamento = f"TRK-{random.randint(10000, 99999)}"
            self.storico_vendite[cod_tracciamento] = prodotto_OBJ
            print(f"{quantita_da_vendere} unità di {prodotto_OBJ.nome} vendute, Rimanenti: {prodotto_OBJ.unita}, Codice Tracking: {cod_tracciamento}\n")
            
            # self.zero_checker()
            vendita = prodotto_OBJ.calcola_profitto(quantita_da_vendere)
            return vendita
        else:
            print("ERRORE: Prodotto non trovato o quantità non valida.")
            
    def stampa_tracking_attivi(self):
        ''' Visualizza tutti i codici tracking generati e non ancora resi '''
        
        print(f"--- TRACKING ATTIVI ({self.nome}) ---")
        if not self.storico_vendite:
            print("Nessuna spedizione attiva.")
            return None
        else:
            for trk, obj in self.storico_vendite.items():
                print(f"Codice: {trk} | Prodotto: {obj.nome}")
        print("--------------------------------------")
        return True
            
    @log_func    
    def resi_prodotto(self, cod_tracciamento: str, unita: int=1):
        prodotto_storico = self.storico_vendite.get(cod_tracciamento)
        
        if prodotto_storico:
    
            if prodotto_storico.nome in self.inventario:
                self.inventario[prodotto_storico.nome].unita += unita
                print(f"Reso accettato: aggiunte {unita} unità a {prodotto_storico.nome}.")
                
            else:
                prodotto_storico.unita = unita
                self.inventario[prodotto_storico.nome] = prodotto_storico
                
            del self.storico_vendite[cod_tracciamento]
            print(f"Reso completato per {prodotto_storico.nome} (ID: {cod_tracciamento})")
            return True
        
        else:
            print(f"ERRORE: Codice {cod_tracciamento} non trovato nello storico.")
            return False

def play():
    mia_fabbrica = Fabbrica("MARCO FABBRICA")
    
    while True:
        print(f"\n=== GESTIONALE {mia_fabbrica.nome.upper()} ===")
        print("1) Aggiungi Prodotto")
        print("2) Vendi Prodotto")
        print("3) Gestisci Reso")
        print("4) Visualizza Inventario")
        print("5) Visualizza Tracking Attivi")
        print("'back' per uscire.")
        
        scelta = input("\nSeleziona un'opzione: ").strip().lower()
        
        if scelta == 'back':
            print("Chiusura gestionale...")
            break

        # --- AGGIUNGI PRODOTTO ---
        if scelta == '1':
            while True:
                print(f"\nCategorie disponibili: {list(mia_fabbrica.TIPI_PROD.keys())}")
                cat = input("Inserisci categoria (o 'back' per menu principale): ").strip().lower()
                
                if cat == 'back': break
                
                if cat in mia_fabbrica.TIPI_PROD:
                    args = mia_fabbrica.asker(cat)
                    if args:
                        classe = mia_fabbrica.TIPI_PROD[cat]
                        nuovo_p = mia_fabbrica.crea_prodotto(classe, args)
                        mia_fabbrica.aggiungi_prodotto(nuovo_p)
                        break
                else:
                    print("Categoria non valida.")

        # --- VENDI PRODOTTO ---
        elif scelta == '2':
            while True:
                mia_fabbrica.stampa_inventario()
                
                if not mia_fabbrica.stampa_inventario():
                    break
                
                nome_p = input("Nome prodotto da vendere (o 'back'): ").strip()
                if nome_p == 'back': continue
                
                try:
                    qty = int(input("Quantità: "))
                    mia_fabbrica.vendi_prodotto(nome_p, qty)
                    break
                except ValueError:
                    print("Errore: Inserire un numero intero per la quantità.")
                    continue

        # --- GESTISCI RESO ---
        elif scelta == '3':
            while True:
                mia_fabbrica.stampa_tracking_attivi()
                if not mia_fabbrica.stampa_tracking_attivi():
                    break
                
                trk = input("Inserisci codice tracking per reso (o 'back'): ").strip()
                if trk == 'back': continue
                
                mia_fabbrica.resi_prodotto(trk)
                break

        # --- VISUALIZZA INVENTARIO ---
        elif scelta == '4':
            mia_fabbrica.stampa_inventario()
            input("\nPremi invio per continuare...")

        # --- VISUALIZZA TRACKING ---
        elif scelta == '5':
            mia_fabbrica.stampa_tracking_attivi()
            input("\nPremi invio per continuare...")

        else:
            print("Opzione non valida, riprova.")

play()
