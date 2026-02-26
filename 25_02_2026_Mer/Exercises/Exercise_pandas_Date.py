# Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
# telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
# vari attributi del cliente e la loro fedeltà.

# Dataset: 
# ID_Cliente: Identificativo unico per ogni cliente
# Età: Età del cliente
# Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
# Tariffa_Mensile: Quanto il cliente paga al mese
# Dati_Consumati: GB di dati consumati al mese
# Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
# Churn: Se il cliente ha lasciato la compagnia (Sì/No)


# Caricamento e Esplorazione Iniziale:
# Caricare i dati da un file CSV.
# Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
# valori mancanti.

# Pulizia dei Dati:
# Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
# Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

# Analisi Esplorativa dei Dati (EDA):
# Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
# Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
# Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.

# Preparazione dei Dati per la Modellazione:
# Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
# Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.

import pandas as pd
import numpy as np

df = pd.read_csv('ZDeposito_csv_txt/clienti_telecom.csv')

print("--- Prime 5 righe ---")
print(df.head())

print("\n--- FASE: ESPLORATIVA NIZIALE ---\n")

print("\n--- info schema ---")
print(df.info())

print("\n--- descrizione (media, deviazione standard, minimi e massimi)---")
# 'all' per vedere statistiche anche sulle colonne testuali
print(df.describe(include='all'))

print("\n--- verifica duplicati ---")
print(df['ID_Cliente'].value_counts())

print("\n--- verifica dati mancanti ---")
#righe che hanno almeno un valore NaN
righe_con_nan = df[df.isnull().any(axis=1)]
print(righe_con_nan)

print("\n--- FASE: PULIZIA DATI ---\n")

# Gestione valori mancanti:
print("approssimazione Eta mancanti...")
df['Età'] = df['Età'].fillna(df['Età'].median())

# Rimozione righe dove mancano dati critici (es. Churn o Tariffa)
print("Rimozione righe dove mancano dati critici (Churn )...")
df.dropna(subset=['Churn'], inplace=True)

# TODO : Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
# Controllo anomalie 
anomalie_eta = df[(df['Età'] < 18)]
anomalie_tariffa = df[(df['Tariffa_Mensile'] <= 0) | (df['Tariffa_Mensile'] > 200)]

print(f"Righe con anomalie età : {len(anomalie_eta)}")
print(anomalie_eta)
print(f"Righe con anomalie tariffa : {len(anomalie_tariffa)}")
print(anomalie_tariffa)

print("\npulizia anomalie")
# Mantiene solo i maggiorenni
print("correzione anomalie età minorenni...")
df = df[df['Età'] >= 18]

print("correzione anomalie tariffa approx...")
# 1. calcolo mediana solo sulle tariffe sensose (tra 0 e 200)
tariffa_mediana = df[(df['Tariffa_Mensile'] > 0) & (df['Tariffa_Mensile'] <= 200)]['Tariffa_Mensile'].median()
df.loc[anomalie_tariffa.index, 'Tariffa_Mensile'] = tariffa_mediana

print("\n --- Dataframe Pulito : ---")
print(df)

print("\n--- FASE: ANALISI ESPLORATIVA (EDA) ---")
# Calcolo costo per GB consumato
# np.where per evitare divisioni per zero se Dati_Consumati è 0
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati'].replace(0, np.nan)
df['Costo_per_GB'] = df['Costo_per_GB'].fillna(0) # o un valore di default

print("\ninserimento Colonna (Costo_per_GB):\n")
print(df[['Tariffa_Mensile', 'Dati_Consumati', 'Costo_per_GB']].head())

# Analisi media per Churn
analisi_churn = df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Servizio_Clienti_Contatti']].mean()
print("\nMedia delle variabili basata sul Churn:")# per vedere se i clienti che se ne vanno hanno caratteristiche comuni:
print(analisi_churn)

# Calcolo correlazione (solo colonne numeriche)
# conversione in int di chur per la vis. in cor()
df['Churn_Numeric'] = df['Churn'].replace({'Sì': 1, 'No': 0})

matrice_corr = df.select_dtypes(include=[np.number]).corr()
print("\nMatrice di Correlazione:")
print(matrice_corr['Churn_Numeric'].sort_values(ascending=False))

# PER CAPIRE: 
#    - Se la correlazione tra Servizio_Clienti_Contatti e Churn_Numeric è alta (es. > 0.6), 
#        significa che troppi contatti all'assistenza sono un segnale quasi certo di abbandono.
#    - Se il Costo_per_GB è molto più alto per chi fa Churn, 
#        la strategia tariffaria potrebbe non essere competitiva per i "heavy users".


print("--- DATAFARME IN OUTPUT:---")
print(df)