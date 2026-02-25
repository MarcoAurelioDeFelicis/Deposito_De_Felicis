# Esercizio 1: Analisi Esplorativa dei Dati


# Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
# usando pandas.


# Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
# un gruppo di persone: Nome, Età, Città e Salario.


# Caricare i dati in un DataFrame autogenerandoli casualmente .

# Visualizzare le prime e le ultime cinque righe del DataFrame.

# Visualizzare il tipo di dati di ciascuna colonna.

# Calcolare statistiche descrittive di base per le colonne numeriche (media,
# mediana, deviazione standard).

# Identificare e rimuovere eventuali duplicati.

# Gestire i valori mancanti sostituendoli con la mediana della rispettiva
# colonna.

# Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
# persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
# anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

# Salvare il DataFrame pulito in un nuovo file CSV.

import pandas as pd

df_input = pd.read_csv('ZDeposito_csv_txt/dataset_nome_eta_citta_salario.csv')
print("Dataframe di input", df_input)

# -- FASE: Preprocessing --
print("-- FASE: Preprocessing --")

# Rimozione dei duplicati
df = df_input.drop_duplicates()

# Gestione dei dati mancanti
df = df.dropna()

# sostituiresistituizione dati mancanti con valore di default
df['Età'].fillna(df['Età'].mean(), inplace=True)
print("Dataframe di Pulito\n", df)

# Aggiungiamo una nuova colonna la persona maggiorenne
df['Giovane'] = df['Età'].between(18, 25, inclusive='both')
# df['Adulto'] = df['Età'] in range(18, 55)
df['Adulto'] = df['Età'].between(26, 55, inclusive='both')
df['Senior'] = df['Età'] >=56
print("\nDataFrame con Categoria Età BOOL:\n", df)

#.loc per trovare righe che soddisfano una condizione e agire solo su una determinata colonna
#df.loc[indice_riga, nome_colonna]
df.loc[df['Età'].between(18, 25), 'Categoria_Età'] = 'Giovane'
df.loc[df['Età'].between(26, 55), 'Categoria_Età'] = 'Adulto'
df.loc[df['Età'] >= 56, 'Categoria_Età'] = 'Senior'
print("\nDataFrame con Categoria Età .loc:\n", df)

# -- FAsE: Analisi -- 
print("\n\n-- FAsE: Analisi -- ")
print("\nPrime 5 righe", df.head(6))

print("\n\nINFO:\n")
print(df.info())

print("\nTipi di dati delle colonne:")
print(df.dtypes)

statistiche = df.describe()
print("\nStatistiche descrittive complete:")
print(statistiche)

media_salario = df['Salario'].mean()
mediana_salario = df['Salario'].median()
deviazione_salario = df['Salario'].std()

media_eta = df['Età'].mean()
mediana_eta = df['Età'].median()
deviazione_eta = df['Età'].std()


print(f"\n\n--- Focus Dati ---")
print(f"Salario Medio: {media_salario} €")
print(f"Mediana Salario: {mediana_salario} €")
print(f"Deviazione Standard Salario: {deviazione_salario} €")
print("\n")
print(f"Media Età: {media_eta} anni")
print(f"Mediana Età: {mediana_eta} anni")
print(f"Deviazione Standard Età: {deviazione_eta} €")

#-- SALVATAGGIO DF --
# Di default, Pandas salva anche la colonna degli indici (0, 1, 2...). 
# Se non metti False, ogni volta che riaprirai il file ti troverai una colonna "Unnamed: 0" in più, 
# creando un pasticcio di duplicati.
df.to_csv('ZDeposito_csv_txt/DsPulito_nome_eta_citta_salario.csv', index=False)
print("dataset Pulito salvato")