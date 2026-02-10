import datetime



# Deve esserci una classe Magazzino che 
# contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, 
# cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

class Magazzino():
    def __init__(self, nome):
        self.nome = nome
        self.aperto = False
        self.inventario = {}
        self.incasso = 0.0
        self.ordini = []
        
    class Pacco():
        # Il sistema deve includere una classe Pacco con: 
        # codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"), 
        # con un metodo per mostrare le info e un metodo per cambiare stato.
        
        stato = set("in magazzino", "in consegna", "consegnato")
        
        def __init__(self, codice:set, peso:int, stato):
            self.codice = codice
            self.peso = peso
            self.stato = stato

        def __str__(self):
            return f"- PACCO: '{self.codice}' | pes0: {self.peso}kl | stato:({self.stato} pag.)"
        
    class GestorePacchi():
        #TODO: aggiungere le funzioni : usa il magazzino per mettere un pacco “in consegna”, 
        # segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.
        pass
        
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
    def aggiungi_pacco(self, nome, prezzo, quantita):
        nome = nome.capitalize()
        if nome in self.inventario:
            self.inventario[nome]['quantita'] += quantita
            #TODO: se quantità 0 lo rimuove da magazino
            print(f"Aggiornata scorta di {nome}. Nuova quantità: {self.inventario[nome]['quantita']}")
        else:
            self.inventario[nome] = {'prezzo': prezzo, 'quantita': quantita}
            print(f"Articolo '{nome}' inserito correttamente.")
    #6
    def rimuovi_pacco(self, nome):
        nome = nome.capitalize()
        if nome in self.inventario:
            del self.inventario[nome]
            print(f"Articolo '{nome}' rimosso dal sistema.")
        else:
            print(f"Errore: '{nome}' non trovato in inventario.")
    #7
    def aggiorna_pacco(self, nome, nuovo_prezzo=None, nuova_quantita=None):
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