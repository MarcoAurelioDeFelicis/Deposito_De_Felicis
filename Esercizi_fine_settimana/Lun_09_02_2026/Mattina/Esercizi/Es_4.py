class Ristorante():
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina 
        self.aperto = False
        self.menu = {}
        
    def descrivi_ristorante(self):
        print(f"Il ristorante '{self.nome}' offre cucina di tipo {self.tipo_cucina}.")
        
    def stato_apertura(self):
        ''' Torna lo stato del ristorante '''
        #TODO: valutare se inserirre la logica di cambio dello stato direttamente qiui
        print (f"STATO RISTORANTE: aperto = {self.aperto}")
    
    def apri_ristorante(self):
        ''' Cambia lo stato apertura in True'''
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora APERTO!")

    def chiudi_ristorante(self):
        ''' Cambia lo stato apertura in False'''
        self.aperto = False
        print(f"Il ristorante {self.nome} è ora CHIUSO.")
        
    def aggiungi_al_menu(self, piatto, prezzo):
        """ Aggiunge il piatto e prezzo nel dizionario """
        self.menu[piatto] = prezzo
        print(f"Aggiunto: {piatto} - {prezzo}€")

    def togli_dal_menu(self, piatto):
        """ fa delete del piatto dla dizionario """
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Rimosso: {piatto}")
        else:
            print(f"Errore: {piatto} non è presente nel menu.")
            
    def stampa_menu(self):
        print(f"\n--- MENU DI {self.nome.upper()} ---")
        if not self.menu:
            print("Il menu è attualmente vuoto.")
        for piatto, prezzo in self.menu.items():
            print(f"- {piatto}: {prezzo:.2f}€")
        print("--------------------------\n")
            
# --- Test ---
# mio_ristorante = Ristorante("Da Mario", "Italiana")

# # Descrizione e stato iniziale
# mio_ristorante.descrivi_ristorante()
# mio_ristorante.stato_apertura()

# # Gestione Menu
# mio_ristorante.aggiungi_al_menu("Carbonara", 12.0)
# mio_ristorante.aggiungi_al_menu("Pizza Margherita", 8.5)
# mio_ristorante.stampa_menu()

# # Apertura e chiusura
# mio_ristorante.apri_ristorante()
# mio_ristorante.stato_apertura()

# # Rimozione piatto
# mio_ristorante.togli_dal_menu("Carbonara")
# mio_ristorante.stampa_menu()

def play():
    print("--- BENVENUTO NEL GESTIONALE RISTORANTI ---")
    nome_r = input("Inserisci il nome del tuo ristorante: ")
    tipo_r = input("Che tipo di cucina offri?: ")
    
    mio_ristorante = Ristorante(nome_r, tipo_r)
    
    while True:
        print("\nCosa vuoi fare?")
        print("1. Descrizione e Stato")
        print("2. Apri Ristorante")
        print("3. Chiudi Ristorante")
        print("4. Aggiungi piatto al menu")
        print("5. Togli piatto dal menu")
        print("6. Stampa Menu")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione: ")

        if scelta == "1":
            mio_ristorante.descrivi_ristorante()
            mio_ristorante.stato_apertura()
        
        elif scelta == "2":
            mio_ristorante.apri_ristorante()
        
        elif scelta == "3":
            mio_ristorante.chiudi_ristorante()
            
        elif scelta == "4":
            nome_p = input("Nome del piatto: ")
            try:
                prezzo_p = float(input("Prezzo: "))
                mio_ristorante.aggiungi_al_menu(nome_p, prezzo_p)
            except ValueError:
                print("Errore: Inserisci un prezzo numerico valido!")
        
        elif scelta == "5":
            nome_p = input("Quale piatto vuoi rimuovere?: ")
            mio_ristorante.togli_dal_menu(nome_p)
            
        elif scelta == "6":
            mio_ristorante.stampa_menu()
            
        elif scelta == "0":
            print(f"Grazie per aver usato il gestionale di {mio_ristorante.nome}. Arrivederci!")
            break
        else:
            print("Opzione non valida, riprova.")
            
play()