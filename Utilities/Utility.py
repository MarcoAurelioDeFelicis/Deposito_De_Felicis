import inspect

# Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

# # ---  USA QUESTA FUNC PER CREARE DOMANDE DINAMICHE IN BASE ALLA CLASSE----
# TIPI_PROD = {"elettronica": Elettronica, "abbigliamento": Abbigliamento} #categorie 

def asker(self, categoria: str):
        ''' Trova i parametri necessari e chiede l'input all'utente '''
        if categoria.lower() == 'back':
            return None
        
        classe_scelta = self.TIPI_PROD.get(categoria)
                
        #firma del metodo __init__
        parametri = inspect.signature(classe_scelta.__init__).parameters
        
        args_da_passare = []
        
        print(f"\n--- Configurazione prodotto {classe_scelta.__name__} ---")
        for nome_param, param in parametri.items():
            # Skip 'self'
            if nome_param == 'self': continue
            
            valore_input = input(f"Inserisci {nome_param}: ")
            #default str perche input è gia str
            tipo_atteso = param.annotation if param.annotation != inspect.Parameter.empty else str
            
            try:
                valore_convertito = tipo_atteso(valore_input)
                args_da_passare.append(valore_convertito)
            except ValueError:
                print(f"ERRORE: '{valore_input}' non è un valore valido per {tipo_atteso.__name__}.")
                return None
                # args_da_passare.append(valore_input) 
                    
        return args_da_passare