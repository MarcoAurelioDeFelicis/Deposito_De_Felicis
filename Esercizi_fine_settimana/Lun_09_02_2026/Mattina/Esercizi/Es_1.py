# Esercizio 1 (Facile):
# Crea una classe chiamata Punto. Questa classe dovrebbe avere:
# Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):
        """Modifica le coordinate dell'istanza."""
        self.x += dx
        self.y += dy
        
    def distanza_da_origine(self):
        """Metodo d'istanza che sfrutta il metodo statico interno ."""
        return self.calcola_distanza(self.x, self.y)

    @staticmethod
    def calcola_distanza(x, y):
        """Calcola la distanza tra due coordinate."""
        return math.sqrt(x**2 + y**2)

def esegui_programma():
    try:
        # Input iniziale
        x = float(input("Coordinata X: "))
        y = float(input("Coordinata Y: "))
        p_OBJ = Punto(x, y)
        
        print(f"Distanza attuale: tra(x:{x}) e(y:{y}) : {p_OBJ.distanza_da_origine():.2f}")

        # Input per il movimento
        dx = float(input("\nSpostamento DX: "))
        dy = float(input("Spostamento DY: "))
        p_OBJ.muovi(dx, dy)

        print(f"Nuova posizione: ({p_OBJ.x}, {p_OBJ.y})")
        print(f"Nuova distanza: {p_OBJ.distanza_da_origine():.2f}")

    except ValueError:
        print("Per favore, inserisci un numero valido.")

esegui_programma()

        