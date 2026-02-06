#Wrapper è una funzione interna ai decoratori che avvoge la funzione originale 
# permette di aggiungere feature extra prima o dopo la funzione decorata, 
# senza alterarne il codice alla radice
# serve per accettare qualsiasi argomento passato tra i parametri, usa il modulo * per splattare

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è ", somma(3, 4))