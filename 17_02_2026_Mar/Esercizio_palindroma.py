

def is_palindroma (parola: str):
    errore = (f"l'imput {parola} non è una parola")
    
    if parola.isdigit():
        print(errore)
        return False
    
    
    parola = parola.replace(" ", "")
    contrario = parola[::-1]
    
    if parola.replace(" ", "") == contrario:
        print(f"SI: {parola} è palindroma")
        print(f"Il contrario : {contrario}")
    else :
        print(f"Il contrario : {contrario}")
        print(f"NO: {parola} NON è palindroma")



while True:
    parola = input("\nscrivi una parola o '0' ").lower()
    if parola == "0":
        break
    
    result = is_palindroma(parola)
    if not result:
        continue 