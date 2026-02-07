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

# print(elenco_tabelle.values())
nome_tab = "utenti"
print(elenco_tabelle.get(nome_tab))
