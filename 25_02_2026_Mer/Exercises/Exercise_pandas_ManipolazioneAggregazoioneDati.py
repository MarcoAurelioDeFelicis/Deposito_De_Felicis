import pandas as pd

def calcola_vendite(df, mode:str):
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    
    if mode == "Tot":
        return df 
    elif mode == "Group":
        ragruppamento = df.groupby('Prodotto')['Totale Vendite'].sum().reset_index()
        return ragruppamento
    else:
        return None
    
def trova_bestseller(df):
    report_q = df.groupby('Prodotto')['Quantità'].sum()
    
    best_seller_nome = report_q.idxmax()
    best_seller_valore = report_q.max()

    return best_seller_nome , best_seller_valore

def trova_best_citta(df):
    vendite_per_citta = df.groupby('Città')['Totale Vendite'].sum()
    citta_top = vendite_per_citta.idxmax()
    valore_top = vendite_per_citta.max()
    
    return citta_top, valore_top

# Caricamento file
df = pd.read_csv('ZDeposito_csv_txt/vendite_citta.csv')

# Aggiunta colonna totale
df = calcola_vendite(df, 'Tot')
print("\n--- Dataframe con colonna Totale ---\n", df)

# Raggruppamento
df_raggruppato = calcola_vendite(df, 'Group')
print("\n--- Report Raggruppato per Prodotto ---\n", df_raggruppato)

# Prodotto BestSeller
best_seller_nome , best_seller_valore = trova_bestseller(df)
print (f"\nIl prodotto più venduto è '{best_seller_nome}' con {best_seller_valore} unità.")

# Citta con maggiorn num di incasso
citta_top , valore_top = trova_best_citta(df)
print(f"\nLa città con il maggior volume di vendite è {citta_top} con un totale di {valore_top}€")

#Creazione New DF FILTRATO
soglia = 1000
#"Prendi df dove la colonna Totale Vendite è maggiore di soglia"
df_vendite_top = df[df['Totale Vendite'] > soglia].copy()
print(f"\n--- Vendite superiori a {soglia}€ ---")
print(df_vendite_top)
print(f"\nNumero di vendite record: {len(df_vendite_top)}")

df_vendite_top.to_csv('ZDeposito_csv_txt/Vendite_record.csv', index=False)
print("\ndataset Vendite_record salvato!!!!!!")
