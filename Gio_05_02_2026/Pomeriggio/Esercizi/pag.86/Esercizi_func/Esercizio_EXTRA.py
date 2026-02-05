def convertitore(user):
    print(f"valore in entrate {user}")
    if isinstance(user, list):
        user = tuple(user)
    elif isinstance(user, tuple):
        user = list(user)
    return user

lista = [2,4,2,"d"]
print(convertitore(lista))

tupla = (2,4,"d","P")
print(convertitore(tupla))