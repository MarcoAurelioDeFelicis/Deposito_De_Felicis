#Classe Base

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_info(self):
        print(f"Veicolo marca: {self.marca}, modello: {self.modello}")
        
class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print("DOtazioni speciali")
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni: list, cavalli):
        Veicolo.__init__(marca, modello)
        #Alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cvalli = cavalli
    
    def mostra_info(self):
        super().mostra_info()
        print(f"potenza cav {self.cvalli}")
        super().mostra_dotazioni()
        
auto_sportiva = AutomobileSportiva("Ferrari", "F40", ["ABS", "Bi Turbo"], 720)
auto_sportiva = AutomobileSportiva("Ferrari", "F40", ["ABS", "Bi Turbo"], 720)
auto_sportiva.mostra_info