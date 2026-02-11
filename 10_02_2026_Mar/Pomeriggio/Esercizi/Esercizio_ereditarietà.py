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
    def __init__(self, nome, costo_produzione, prezzo_vendita, unita, categoria, componenti: list, classe_energetica: str):
        super().__init__(nome, costo_produzione, prezzo_vendita, unita, categoria)
        self.componenti = componenti
        self.classe_energetica = classe_energetica
        
    def __str__(self):
        return f"(Categoria: {self.categoria}) " + super().__str__() 

# --- CLASSE ABBIGLIAMENTO(Prodotto) ---
class Abbigliamento(Prodotto):    
    
    taglie_disponibili = ("XL","L","M","S","XS" )
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, unita, categoria, materiale: str, taglia:str):
        super().__init__(nome, costo_produzione, prezzo_vendita, unita, categoria)
        self.materiale = materiale
        self.taglia = taglia
        
    def __str__(self):
        return f"(Categoria: {self.categoria}) " + super().__str__() 
        

# --- CLASSE FABBRICA ---
class Fabbrica:
    TIPI_PROD = {"elettronica": Elettronica, "abbigliamento": Abbigliamento}
    
    def __init__(self, nome, inventario=None):
        if inventario is None:
            inventario = {}
        self.storico_vendite = []
        self.nome = nome
        
#-------------- METODI --------------------------------------------
        
    def stampa_inventario(self):
        print(f"--- INVENTARIO DI: {self.nome.lower()} ---")
        if not self.inventario:
            print("Il magazzino è vuoto.")
        else:
            # Iteriamo sui valori (gli oggetti Pacco)
            for p in self.inventario.values():
                print(p) #__str__ di Pacco
        print("----------------------------------")
    
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
            
    def asker(self, classe_scelta):
        ''' Trova i parametri necessari e chiede l'input all'utente '''
        #firma del metodo __init__
        parametri = inspect.signature(classe_scelta.__init__).parameters
        
        args_da_passare = []
        
        print(f"\n--- Configurazione {classe_scelta.name} ---")
        for nome_param, param in parametri.items():
            # Skip 'self'
            if nome_param == 'self':
                continue
            
            valore = input(f"Inserisci {nome_param}: ")
            
            # TODO : Qui potrei aggiungere una logica per convertire in int/float
            # Per ora li lascio come stringhe o cast base
            args_da_passare.append(valore)
            
        return args_da_passare
    
    @log_func
    @zero_checker   
    def crea_prodotto(self, classe_scelta, args_lista):
        ''' Spacchetta * gli argomenti e istanzia OBJ della classe '''
        try:
            # L'operatore * trasforma la lista [a, b, c] in (a, b, c) passati come argomenti
            new_OBJ = classe_scelta(*args_lista)
            
            # Lo aggiungiamo all'inventario usando il nome come chiave
            self.inventario[new_OBJ.nome] = new_OBJ
            print(f"SUCCESSO! {new_OBJ.nome} creato e aggiunto!")
            return new_OBJ
        except Exception as e:
            print(f"ERRORE: durante la creazione: {e}")


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
            print(f"{quantita_da_vendere} unita di {prodotto_OBJ.nome} vendute, Rimanenti: {prodotto_OBJ.unita} un\n")
            
            # self.zero_checker()
            #TODO: se quantità scende a 0 allora viene rimosso da magazzino
            vendita = prodotto_OBJ.calcola_profitto(quantita_da_vendere)
            return vendita
        else:
            print("ERRORE: Prodotto non trovato o quantità non valida.")
            
    @log_func    
    def resi_prodotto(self, prodotto: Prodotto, unita: int=1):
        if  prodotto in self.storico_vendite:
            # TODO : logica: se il prodotto è in magazzino, allora +1 a prodotto.unità else lo ricrea e lo pusha in magazzino
            return
        else:
            print("ERRORE: Prodotto non trovato o quantità non valida.")
        