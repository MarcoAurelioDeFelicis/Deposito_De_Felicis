# Andiamo a creare un sistema ripetibile che simuli un teatro:

# Classe Base: Posto
# Attributi privati:
# _numero (intero): il numero del posto.
# _fila (stringa): la fila in cui si trova il posto.
# _occupato (booleano): stato del posto, se è occupato (True) o libero (False).
# Metodi:
# __init__(numero, fila): inizializza il posto impostando _occupato a False.
# prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
# libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
# Getter: per recuperare il numero, la fila e lo stato (occupato/libero).

# Classi Derivate
# PostoVIP:
# Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
# Metodi:
# Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
# PostoStandard:
# Attributi aggiuntivi: costo

# Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
# Metodi:
# Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.

# Classe Teatro
# Attributi:
# _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
# Metodi:
# aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
# prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
# stampa_posti_occupati(): stampa tutti i posti che risultano occupati.

class Posto:
    def __init__(self, numero: int, fila: str ):
        self._numero = numero
        self._fila = fila.upper()
        self._occupato = False
        
    def get_numero(self):
        return self._numero
    
    def get_fila(self):
        return self._fila
    
    def is_occupato(self):
        return self._occupato
        
    def get_info(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Fila: {self._fila} Numero: {self._numero} [{stato}]"
        
    def prenota(self, cliente):
        if self._occupato:
            print(f"Errore: Il posto {self._fila}{self._numero} è già occupato.")
            return False
        else:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato con successo da: {cliente}")
            return True
        
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} ora è libero.")
        else:
            print(f"ℹIl posto {self._fila}{self._numero} non era prenotato.")

class Teatro:
    
    TIPI_TEATRO = {
        'piccolo': 20,
        'medio': 100,
            'grande': 1000
                }
        
    def __init__(self, nome:str, tipo_teatro : str):
        self.nome = nome
        self._posti = ()
        if tipo_teatro not in self.TIPI_TEATRO:
            raise ValueError(f"Tipo teatro non valido. Scegli tra: {list(self.TIPI_TEATRO.keys())}")
        self.tipo_teatro = tipo_teatro
        self.limite_posti = self.TIPI_TEATRO[tipo_teatro]
        
    def aggiungi_posto(self, posto: Posto):
        if len(self._posti) >= self.limite_posti:
            print("Capacità massima raggiunta! Sold out.")
            return None
        
        for p_dict in self._posti:
            if p_dict['fila'] == posto.get_fila() and p_dict['numero'] == posto.get_numero():
                print(f"⚠️ Errore: Il posto {posto.get_fila()}{posto.get_numero()} esiste già.")
                return
        
        nuovo_posto_dict = {
            'fila': posto._fila,
            'numero': posto._numero,
            'info_posto': posto
        }

        self._posti = self._posti + (nuovo_posto_dict,)
        print(f"Posto {posto.get_fila()}{posto.get_numero()} aggiunto correttamente.")
        
    def prenota_posto(self, fila, numero, cliente):
        for p_dict in self._posti:
            if p_dict['fila'] == fila.upper() and p_dict['numero'] == numero:
                # p_OBJ = TODO: logica pescaggio kiavi dct e get dell'ogetto da self.posti 
                # per poi chiamare il suo metodo prenota
                return
        print("Posto non trovato.")
        
        
        
# --- TEST ---
def play():
    print("=== BENVENUTO NEL GESTORE TEATRO ===")
    n_teatro = input("Nome del teatro: ")
    tipo_t = input("Dimensione (piccolo/medio/grande): ").lower()
    
    try:
        t = Teatro(n_teatro, tipo_t)
    except ValueError as e:
        print(e)
        return

    while True:
        print(f"\n--- Menu {t.nome} ---")
        print("1. Aggiungi Posto (Configurazione)")
        print("2. Prenota Posto")
        print("0. Esci")
        
        scelta = input("Scelta: ")

        if scelta == "1":
            f = input("Fila (es. A): ")
            try:
                n = int(input("Numero: "))
                p_OBJ = Posto(numero= n , fila= f)
                t.aggiungi_posto(p_OBJ)
            except ValueError:
                print("Numero non valido.")

        elif scelta == "2":
            f = input("Fila: ")
            try:
                n = int(input("Numero: "))
                c = input("Nome Cliente: ")
                t.prenota_posto(f, n, c)
            except ValueError:
                print("Dati non validi.")

        elif scelta == "0":
            break

if __name__ == "__main__":
    play()