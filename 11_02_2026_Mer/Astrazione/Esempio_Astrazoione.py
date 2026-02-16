from abc import ABC, abstractmethod

class Animale (ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane (Animale):
    def __init__(self):
        super().__init__()
        
    def muovi(self):
        print("CORRO")

class Pesce (Animale):
    def muovi(self):
        print ("NUOTO")
    
doggo = Cane()
azione1 = doggo.muovi
print(azione1)

nemo = Pesce()
print(nemo.muovi)

