# Spiegazione ed Esempio di Caricamento del File CSV:
# Per caricare i dati da un file CSV utilizzando pandas, segue un esempio di codice Python.
# Questo processo è tipico per l'inizio di un'analisi dei dati, dove i dati vengono prima caricati
# in un DataFrame, che è la struttura dati primaria in pandas.

import pandas as pd

# Percorso del file CSV
file_path = '25_02_2026_Mer/Files_csv/città_latine.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)
#le prime righe del DataFrame per confermare
print(df.head())