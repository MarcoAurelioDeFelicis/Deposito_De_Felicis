import pandas as pd

print(" -- PVOT -- ")
# Dati di esempio
data = {
'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)
print(df)

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("\n")
print(pivot_df)
 
print("\n\n -- GROUPBY -- ")
# Dati di esempio
data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
    }
df = pd. DataFrame(data)
# Utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto') .sum()
print (grouped_df)

print("\n\n -- MODIFICA AGGIORNAMENTO E PULIZIA DATI --")
# Creazione dei DataFrame
data_vendite = {
'Prodotto': ['Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor'],
'Quantità': [5, 10, 2, 7, 3],
'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano'],
'Data': ['2021-09-01', '2021-09-01', '2021-09-02', '2021-09-02', '2021-09-03']
}
vendite_df = pd.DataFrame(data_vendite)

data_costi = {
'Prodotto': ['Tastiera', 'Mouse', 'Monitor'],
'Costo per unità': [50, 25, 150]
}
costi_df = pd.DataFrame(data_costi)

# Unione dei DataFrame
df_merge = pd.merge(vendite_df, costi_df, on='Prodotto')

# Creazione della tabella pivot
pivot_table = df_merge.pivot_table(index='Prodotto', columns='Città', values='Quantità', aggfunc='sum')

# Visualizzazione del risultato
print(pivot_table)