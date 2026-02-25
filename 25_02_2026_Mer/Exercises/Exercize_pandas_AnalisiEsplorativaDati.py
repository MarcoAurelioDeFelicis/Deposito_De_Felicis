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
print("Dataframe di Pulito", df)


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