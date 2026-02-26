# Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite generato casualmente,
# applicando le tecniche di pivot e groupby.

# Descrizione: Gli studenti dovranno generare un DataFrame di vendite che include i seguenti campi: 
# "Data", "Città", "Prodotto" e "Vendite". 
# I dati devono essere generati per un periodo di un mese, 
# con vendite registrate per tre diverse città e tre tipi di prodotti.

# 1.⁠ ⁠Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.

# 2.⁠ ⁠Creazione della Tabella Pivot: Creare una tabella pivot per analizzare 
# le vendite medie di ciascun prodotto per città.

# 3.⁠ ⁠Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare Le vendite totali per ogni prodotto.


import pandas as pd
import numpy as np
# from datetime import date

# config parametri
n_righe = 100  
citta_lista = ['Roma', 'Milano', 'Napoli', 'Vilnius', 'Torino']
prodotti_lista = ['Smartphone', 'Laptop', 'Tablet', "webcam"]
date = [2020, 2022, 1999, 1992, 1987, 2001, 2026]

# Generazione NumPy
# np.random.choice per selezionare elementi casuali dalle liste
date_casuali = np.random.choice(date, n_righe)
citta_casuali = np.random.choice(citta_lista, n_righe)
prodotti_casuali = np.random.choice(prodotti_lista, n_righe)
# np.random.uniform per generare prezzi casuali tra 100 e 2000 
vendite_casuali = np.random.uniform(100, 2000, n_righe).round(2)

#DataFrame
df = pd.DataFrame({
    'Data': date_casuali,
    'Città': citta_casuali,
    'Prodotto': prodotti_casuali,
    'Vendite': vendite_casuali
})

# Ordniamento per data
df = df.sort_values(by='Data').reset_index(drop=True)

print("--- DataFrame Random ---")
print(df)

# # Carichamento file
# df = pd.read_csv('ZDeposito_csv_txt/vendite_mensili.csv', parse_dates=['Data'])

# tipi dati colonne - Schema del datafram
print("Tipi di colonne:")
print(df.dtypes)

# Pivot Table 
pivot_medie = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print("\n--- Vendite Medie per Città e Prodotto ---")
print(pivot_medie.round(2))

# Groupby 'Prodotto' e somma colonna 'Vendite'
vendite_totali_prodotto = df.groupby('Prodotto')['Vendite'].sum().reset_index()

print("\n--- Vendite Totali per Ogni Prodotto ---")
print(vendite_totali_prodotto)