valori = set(("char","bool","int","double","date"))
logged_user = {"utente": "stato"}
utenti = {"mirko": "M123K", "marco": "123A"}
nome_db = "Pizzeria"
scelte = []
data_creazione = 0
elenco_tabelle = {
    "utenti": {"id": "int", "nome": "char"},
    "ordini": {"id": "int"}
}

# print(elenco_tabelle.values())
# nome_tab = "utenti"
# print(elenco_tabelle.get(nome_tab))

db = {'Pizzeria': {'pizza': [['margherita', 8.0], ['rossa', 5.0]]}}

old_param = 'rossa'
nome_tab = 'pizza'
id_row = 1

check = db[nome_db][nome_tab][id_row]
print(check)

if old_param in check:
    idx = check.index(old_param)
    print(f"Found '{old_param}' at index: {idx}")

schema_tab = {'nome': 'char', 'prezzo': 'double'}
tipi_colonne = list(schema_tab.values()) # ["char", "double"]
print(f"DEBUG : tipi_col: {tipi_colonne}")

tipo_atteso = tipi_colonne[idx]
print(f"DEBUG: {tipo_atteso}")