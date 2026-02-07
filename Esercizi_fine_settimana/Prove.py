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


  
  
# TODO: mostra le colonne da schema_tabelle per tabella selezoinata,
#procede alla creazione del record seguendo le regole dello schema, 
#aggiungi un sistema di validazione per il tipo di dato da inserire,
#salva il record in un dizionario db {Pizzeria: {
    #"pizza":[
        #["margherita","pomodoro,mozzarella",8.00],
        #["diavola","pomodoro,salame,mozzarella",10.00]
    # ]
# }