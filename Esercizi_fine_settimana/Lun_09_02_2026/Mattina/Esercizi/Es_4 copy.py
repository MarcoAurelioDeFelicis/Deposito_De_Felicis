class Ristorante():
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = []
        self.incasso = 0.0
        
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
        
    def aggiungi_al_menu(self, nome, prezzo):
        #Istanza di Piatto
        nuovo_piatto_OBJ = self.Piatto(nome, prezzo)
        self.menu.append(nuovo_piatto_OBJ)
        print(f"Aggiunto al menu: {nuovo_piatto_OBJ}")

    def togli_dal_menu(self, nome_da_togliere):
        ''' Cercha l'oggetto che ha quel nome nella lista'''
        original_size = len(self.menu)
        self.menu = [p for p in self.menu if p.nome_piatto.lower() != nome_da_togliere.lower()]
        
        if len(self.menu) < original_size:
            print(f"Rimosso '{nome_da_togliere}' dal menu.")
        else:
            print(f"Piatto '{nome_da_togliere}' non trovato.")
            
    # def fixa_menu(self, nome_da_togliere, nome_da_aggiungere):
    #     #TODO chiama del e poi add
    #     pass
            
    def ordina_piatto(self, nome_piatto):
        # controllo se il ristorante è aperto
        if not self.aperto:
            print(f"Impossibile ordinare: {self.nome} è chiuso!")
            return

        # Ricerca del piatto nel menu (case-insensitive)
        for piatto in self.menu:
            if piatto.nome_piatto.lower() == nome_piatto.lower():
                self.incasso += piatto.prezzo
                print(f"Ordine ricevuto: {piatto.nome_piatto} ({piatto.prezzo:.2f}€)")
                print(f"Incasso totale attuale: {self.incasso:.2f}€")
                return
        
        # se il ciclo finisce senza 'return', il piatto non esiste
        print(f"Mi dispiace, '{nome_piatto}' non è sul menu.")

    def mostra_incasso(self):
        print(f"Totale incassato oggi: {self.incasso:.2f}€")
            
    def stampa_menu(self):
        print(f"\n--- MENU DI {self.nome.upper()} ---")
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            for p in self.menu:
                print(f"- {p}")
        print("--------------------------\n")
    
    def descrivi_ristorante(self):
        print(f"Il ristorante '{self.nome}' offre cucina di tipo {self.tipo_cucina}.")
        
    # --- PIATTO ---
    class Piatto():
        def __init__(self, nome_piatto, prezzo):
            self.nome_piatto = nome_piatto
            self.prezzo = prezzo

        def __str__(self):
            return f"{self.nome_piatto}: {self.prezzo:.2f}€"

def play():
    print("--- BENVENUTO NEL GESTIONALE RISTORANTI ---")
    nome_r = input("Inserisci il nome del tuo ristorante: ")
    tipo_r = input("Che tipo di cucina offri?: ")
    
    mio_ristorante = Ristorante(nome_r, tipo_r)
    
    while True:
        print("\nCosa vuoi fare?")
        print("1) Descrizione e Stato")
        print("2) Apri Ristorante")
        print("3) Chiudi Ristorante")
        print("4) Aggiungi piatto al menu")
        print("5) Togli piatto dal menu")
        print("6) Stampa Menu")        
        print("\n--- GESTIONE CASSA ---")
        print("7. Ordina un piatto")
        print("8. Visualizza Incasso Totale")
        print("")
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
            mio_ristorante.stampa_menu()
            nome_p = input("Quale piatto vuoi rimuovere?: ")
            mio_ristorante.togli_dal_menu(nome_p)
            
        elif scelta == "6":
            mio_ristorante.stampa_menu()
            
        elif scelta == "7":
            if not mio_ristorante.menu:
                print("Il menu è vuoto! Aggiungi prima dei piatti.")
            else:
                if not mio_ristorante.aperto:
                    print("Ristorante Chiuso... ")
                    continue
                else:
                    mio_ristorante.stampa_menu()
                    p_ordinato = input("Cosa desidera ordinare il cliente?: ")
                    mio_ristorante.ordina_piatto(p_ordinato)
        
        elif scelta == "8":
            mio_ristorante.mostra_incasso()
            
        elif scelta == "0":
            print("\nArrivederci!")
            print(f"Incasso finale: {mio_ristorante.incasso:.2f}€")
            break
        else:
            print("Opzione non valida, riprova.")
            
play()