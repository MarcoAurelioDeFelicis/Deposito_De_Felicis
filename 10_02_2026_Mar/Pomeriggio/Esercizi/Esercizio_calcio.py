# lasse MembroSquadra:

# Attributi:
# nome (stringa)
# età (intero)
# Metodi:
# descrivi() (stampa una descrizione generale del membro della squadra)
# Classi Derivate:

# Giocatore:

# Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
# Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
# Allenatore:
# Attributi aggiuntivi come anni_di_esperienza
# Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
# Assistente:
# Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
# Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

# Crea due squadre e falle giocare contro.
import random
import inspect

class Squadra:
    TIPI_PROD = ['allenatore', 'giocatore']
    def __init__(self, squadra: str):
        self.squadra = squadra
        self.formazione = {}
        
    def stampa_formazione(self):
        print(f"--- INVENTARIO DI: {self.nome.lower()} ---")
        if not self.formazione:
            print("Il magazzino è vuoto.")
            return None
        else:
            # Iteriamo sui valori (gli oggetti Pacco)
            for p in self.formazione.values():
                print(p) #__str__ di Pacco
        print("----------------------------------")
        return True
        
    def asker(self, categoria: str):
        ''' Trova i parametri necessari e chiede l'input all'utente '''
        if categoria.lower() == 'back':
            return None
        
        classe_scelta = self.TIPI_PROD.get(categoria)
                
        #firma del metodo __init__
        parametri = inspect.signature(classe_scelta.__init__).parameters
        
        args_da_passare = []
        
        print(f"\n--- Configurazione Persona {classe_scelta.__name__} ---")
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
            
    def inserisci_giocatore(self, classe_scelta, args_lista):
        ''' Spacchetta * gli argomenti e istanzia OBJ della classe '''
        
        try:
            new_OBJ = classe_scelta(*args_lista)
            return new_OBJ
        
        except Exception as e:
            print(f"ERRORE: durante l'inseromento: {e}")
            return None
        

class MembroSquadra(Squadra):
    def __init__(self, squadra, nome, eta):
        super().__init__(squadra)
        self.nome = nome
        self.eta = eta
        
    def __str__(self):
        return f"MEMBRO: {self.nome}, età: {self.eta}, "
    
class Giocatore(MembroSquadra):
    def __init__(self, squadra, nome, eta, ruolo, numero_maglia):
        super().__init__(squadra, nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.possesso_palla = False
        self.azioni_senza_palla = ['attacca', 'difendi' ] if ruolo != 'portiere' else ['para']
        self.azioni_con_palla = ['dribla', 'passa', 'tira'] if ruolo != 'portiere' else ['passa', 'tira']
        
    def giocapartita(self):
        if self.possesso_palla == True:
            azzione_eseguita = random.choice(self.azioni_con_palla)
        else:
            azzione_eseguita = random.choice(self.azioni_senza_palla)
            
        return azzione_eseguita
    
    def __str__(self):
        return super().__str__() + f"ruolo {self.ruolo}, numero maglia {self.numero_maglia},"
    
class Allenatore(MembroSquadra):
    def __init__(self, squadra, nome, eta, esperienza):
        super().__init__(squadra, nome, eta)
        self.esperienza = esperienza
        self.squadra = squadra
        
    def incita_scuadra(self):
        return f"ALLENATORE: {self.nome} sta motivando la propria squadra {self.squadra}"
    
class Arbritro:
    AMMONIZIONI
    
    def __init__(self, nome: str, cornuto: bool):
        self.nome = nome
        self.cornuto = cornuto
        
         
        
    

    