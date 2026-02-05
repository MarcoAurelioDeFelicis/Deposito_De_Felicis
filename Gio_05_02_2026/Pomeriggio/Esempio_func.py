# La prova pratica dell'astrazione, sono blocchi di codice autonomi e scalanili e riutilizzabili
# che eseguono un a azione specifica:
# caratteristiche:
# modularità = "modulo prefatto che può essere utilizzato in doversi progetti"
# manutenibili = "modificare qualcosa che viene richiamata in varie parti"

def impreca(dude, divinità):
    print(f"{dude} dice: P***+{divinità}!!")
    
impreca("Marco", "Anubi")

def contatore (dude: str, mele: int, pere: int):
    result = mele + pere
    return f"{dude} ha {result} frutti"

def contatore2 (mele: int, pere: int):
    frutta = sum((mele,pere))
    return frutta

mele = 5
pere = 3

print(contatore("mirko".capitalize(), mele, pere))
print(f'{"mirko".capitalize()} ha {contatore2(mele, pere)} frutti')

