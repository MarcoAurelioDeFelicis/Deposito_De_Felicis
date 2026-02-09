class Biblioteca:
    libri = {} 

    def __str__(self):
        return f"La Biblioteca ha {len(self.libri)} libri.\nElenco:\n{self.libri}"

    class Libro:
        def __init__(self, titolo, autore, pagine):
            self.titolo = titolo
            self.autore = autore
            self.pagine = pagine

        def __str__(self):
            return f"- '{self.titolo}' di {self.autore} ({self.pagine} pag.)"

    @classmethod
    def crea_libro(cls):
        """Crea un libro da input e lo aggiunge al dizionario della biblioteca."""
        while True:
            try:
                t = input("Titolo: ")
                a = input("Autore: ")
                p = int(input("Pagine: "))
                
                # Istanza di class Libro
                nuovo_libro_OBJ = cls.Libro(t, a, p)
                
                # Aggiunta al dizionario della classe Biblioteca
                cls.libri[t] = nuovo_libro_OBJ
                print(f"Libro '{t}' aggiunto con successo!")
                break
            
            except ValueError:
                print("Errore: le pagine devono essere un numero!")
                continue

def play():
    mia_biblio = Biblioteca()
    
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Aggiungi un libro")
        print("2. Visualizza tutti i libri")
        print("3. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            Biblioteca.crea_libro()
        elif scelta == "2":
            print("\n--- STATO ATTUALE ---")
            print(mia_biblio)
        elif scelta == "3":
            print("Chiusura programma. Arrivederci!")
            break
        else:
            print("Scelta non valida, riprova.")
play()
