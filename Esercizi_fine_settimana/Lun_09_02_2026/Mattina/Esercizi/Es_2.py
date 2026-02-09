# Esercizio 2 (Facile):
# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def __str__(self):
        return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine."

    @staticmethod
    def e_lungo(pagine):
        """Valuta se un numero di pagine è sopra la media"""
        return pagine > 500

def aggiungi_libro():
    try:
        print("--- Inserimento nuovo libro ---")
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        pagine = int(input("Numero di pagine: "))
        
        # Creazione dell'istanza
        nuovo_libro_OBJ = Libro(titolo, autore, pagine)
        
        # Output della descrizione
        print(f"\nInfo: {nuovo_libro_OBJ}")
        
        # Uso del metodo statico
        if Libro.e_lungo(pagine):
            print("Questo è un libro piuttosto impegnativo!")
        else:
            print("Una lettura di media lunghezza.")
            
    except ValueError:
        print("Errore: Il numero di pagine deve essere un numero intero.")

if __name__ == "__main__":
    aggiungi_libro()
