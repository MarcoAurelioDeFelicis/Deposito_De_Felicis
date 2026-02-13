from abc import ABC, abstractmethod

class Utente(ABC):
    @abstractmethod
    def timbra(self):
        pass

class Dipendente(Utente):
    posizioni_disponibili = ["Fuori", "Dentro"]
    def __init__(self, nome, cognome, badge: int, turni: dict, ruolo: str):
        self.__nome = nome
        self.__cognome = cognome
        self.__badge = badge
        self.__turni = turni
        self.__ruolo = ruolo
        self.__posizione = "Fuori"
        
    # --- Metodi GETTER ---
    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_badge(self):
        return self.__badge

    def get_turni(self):
        return self.__turni

    def get_ruolo(self):
        return self.__ruolo

    def get_posizione(self):
        return self.__posizione

    # --- Metodi SETTER ---

    def set_badge(self, nuovo_badge: int):
        if nuovo_badge > 0:
            self.__badge = nuovo_badge
        else:
            print("Errore: Il numero di badge deve essere positivo.")

    def set_turni(self, nuovi_turni: dict):
        self.__turni = nuovi_turni

    def set_ruolo(self, nuovo_ruolo: str):
        self.__ruolo = nuovo_ruolo

    def set_posizione(self, nuova_posizione: str):
        if nuova_posizione in self.posizioni_disponibili:
            self.__posizione = nuova_posizione
        else:
            print(f"Errore: Stato '{nuova_posizione}' non valido.")
            
    def timbra(self):
        # Usiamo i metodi interni per coerenza
        if self.get_posizione() == "Fuori":
            self.set_posizione("Dentro")
        else:
            self.set_posizione("Fuori")
        return self.get_posizione()

