from datetime import datetime
from Dipendenti import Dipendente

class Porta:
    def __init__(self, nome_porta: str):
        self.nome_porta = nome_porta
        self.storico_accessi = []  

    def registra_passaggio(self, dipendente: Dipendente):
        # cambiamo stato dipendente
        nuovo_stato = dipendente.timbra()
        orario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # record dell'operazione
        evento = {
            "orario": orario,
            "badge": dipendente.get_badge(),
            "nominativo": f"{dipendente.get_nome()} {dipendente.get_cognome()}",
            "azione": "ENTRATA" if nuovo_stato == "Dentro" else "USCITA",
            "porta": self.nome_porta
        }
        
        self.storico_accessi.append(evento)
        
        print(f"[{orario}] {evento['nominativo']} -> {evento['azione']} (Porta: {self.nome_porta})")
        return evento

    def mostra_log(self):
        print(f"\n--- LOG ACCESSI {self.nome_porta.upper()} ---")
        for log in self.storico_accessi:
            print(log)