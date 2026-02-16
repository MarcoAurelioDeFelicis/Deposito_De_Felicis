# Decoratore
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

@log_func
def inserisci():
    while True:
        valore = input("Inserisci: ").strip().lower()
        if valore:
            return valore
        print("Errore: Devi inserire una parola valida.")
        
@log_func        
def dct_char(user: str):
    user = user.replace(" ", "")
    
    
    dizzionario = {}
    
    for l in user:
        if not l in dizzionario:
            dizzionario[l] = user.count(l)
    
    # for lettera in user:
    #     if lettera in dizzionario:
    #         dizzionario[lettera] += 1
    #     else:
    #         dizzionario[lettera] = 1
    # return dizzionario
    
 
user = inserisci().lower()
dizzionario_mappato = dct_char(user)
print(dizzionario_mappato)

