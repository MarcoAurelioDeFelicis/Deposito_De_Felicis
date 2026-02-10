#Classe Base

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome}")