valori = set(("char","bool","int","double","date"))
logged_user = {"utente": "stato"}
utenti = {"mirko": "M123K", "marco": "123A"}
nome_db = ""
scelte = []
data_creazione = 0
elenco_tabelle = {
    "utenti": {"id": "int", "nome": "char"},
    "ordini": {"id": "int"}
}

print(elenco_tabelle.values())

    
def update_scelte():
    global scelte
    global logged_user
    
    scelte = ["crea_db", "exit"] if "logged_lv1" in logged_user.values() else["crea_tab","exit"]
    
    if "mirko" in logged_user.keys():
        scelte.append("crea_new_user")
        
    if len(elenco_tabelle) > 0:
        scelte.append("crea_col")
    elif "crea_col" in scelte and len(elenco_tabelle) < 1:
        scelte.pop("crea_col")
        
    if len([elenco_tabelle.items]) > 0:
        scelte.append("popola")
    elif "popola" in scelte and len(elenco_tabelle.items) > 0:
        scelte.pop("popola")
        
    return scelte
    