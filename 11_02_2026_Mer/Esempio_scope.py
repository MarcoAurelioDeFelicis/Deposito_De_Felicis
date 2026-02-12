numero = 10

def funzione_estera():
    numero = 5
    print(f"numero in esterna = {numero}")
    
    def funzione_interna():
        nonlocal numero
        numero = 3
        print(f"numero in interna = {numero}")
    
    funzione_interna()

play = funzione_estera()
print(play)
    
