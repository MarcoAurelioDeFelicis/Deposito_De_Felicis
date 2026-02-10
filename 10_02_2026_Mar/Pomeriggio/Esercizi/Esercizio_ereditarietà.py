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
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

class Prodotto:
    def __init__(self, nome: str, costo_produzione: float, prezzo_vendita: float, unita: int):
        
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.unita = unita
        
    def calcola_profitto(self, quantita_da_vendere):
        self.unita -= quantita_da_vendere
        profitto = self.prezzo_vendita * quantita_da_vendere - self.costo_produzione * quantita_da_vendere
        print(f"{quantita_da_vendere} unita di  {self.nome} vendute, Rimanenti: {self.unita} un\n")
        print(f"profitto prodotto: {profitto}\n")
        print(f"costo di produzione * unita {self.costo_produzione * quantita_da_vendere}")
        return profitto 
        
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, unita, features: list, classe_energetica: str):
        super().__init__(nome, costo_produzione, prezzo_vendita, unita)

class Abbigliamento(Prodotto):    
    
    taglie_disponibili = ("XL","L","M","S","XS" )
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, unita, materiale: str, taglia:str):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
        self.taglia = taglia

class Fabbrica:
    def __init__(self, inventario={}):
        self.inventario = inventario
        self.storico_vendite = []
        
    def stampa_inventario(self):
        print(f"--- INVENTARIO DI {self.nome.lower()} ---")
        if not self.inventario:
            print("Il magazzino è vuoto.")
        else:
            # Iteriamo sui valori (gli oggetti Pacco)
            for p in self.inventario.values():
                print(p) #__str__ di Pacco
        print("----------------------------------")
        
    @log_func   #def __init__(self, nome: str, costo_produzione: float, prezzo_vendita: float):
    def aggiungi_prodotto(self, prodotto: Prodotto):
        if not prodotto in self.inventario:
            self.inventario[prodotto]
            print(f"prodotto {prodotto.nome} aggiunto all'inventrio\n")
            print(f"Inventario AGGIORNATO : {self.stampa_inventario()}")
        else:
            print("ERRORE")
            
    @log_func        
    def vendi_prodotto(self, prodotto: Prodotto, quantita_da_vendere: int):
        if  prodotto in self.inventario and quantita_da_vendere <= prodotto.unita:
            #TODO: se quantità scende a 0 allora viene rimosso da magazzino
            vendita = prodotto.calcola_profitto(quantita_da_vendere)
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
        