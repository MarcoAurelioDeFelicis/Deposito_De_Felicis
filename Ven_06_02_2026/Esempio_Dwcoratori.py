
def decoratore(funzione):
    def wrapper(nome):
        print("prima")
        funzione(nome)
        print("dopo")
    return wrapper

@decoratore
def saluta(nome):
    print(f"Ciao! {nome}")
    
saluta('Marco')