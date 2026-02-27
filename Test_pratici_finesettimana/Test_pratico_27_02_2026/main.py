import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def genera_dataset_clienti():
    np.random.seed(42)
    n_clienti = 1000
    
    data = {
        'Nome': np.random.choice(['Mario', 'Elena', 'Luca', 'Giulia', 'Sara', None], n_clienti),
        'Eta': np.random.normal(45, 15, n_clienti).astype(int),
        'Bolletta_Unica': np.random.choice(['Sì', 'si', 'SI', 'No', 'nO', 'NO', None], n_clienti),
        'Costo_Mensile_Medio': np.random.uniform(20, 150, n_clienti),
        'Disdetta': np.random.choice(['Sì', 'No', None], n_clienti, p=[0.2, 0.7, 0.1])
    }
    
    df = pd.DataFrame(data)
    
    df['ID_Cliente'] = range(1, n_clienti + 1)
    
    # vado a sporcare i dati
    # età 
    df.loc[np.random.choice(df.index, 20), 'Eta'] = [200, -5, 150, -10] * 5
    # NaN nell'età
    df.loc[np.random.choice(df.index, 50), 'Eta'] = np.nan
    
    return df




def main():
    df = genera_dataset_clienti()
    print("\n---- FASE: ESPLORATIVA NIZIALE ----\n")
    
    print("\n--- info schema ---")
    print(df.info())
    print("\n--- descrizione (media, deviazione standard, minimi e massimi) ---")
    print(df.describe(include='all'))
    
    print("\ndataset sporco:")
    print(df.head(10))
    
    print("\n--- verifica duplicati ---")
    print(df['ID_Cliente'].value_counts())  
    
    print("\n--- verifica dati mancanti ---")
    righe_con_nan = df[df.isnull().any(axis=1)]
    print(righe_con_nan)

    # ----  FASE: PULIZIA DATI  ----
    print("\n----  FASE: PULIZIA DATI  ----\n")

    # PULIZIA ANOMALIE ETÀ (Approssimazione dati mancanti)
    print("pulizzia e approssimazione Eta ...")
    df.loc[(df['Eta'] < 18) | (df['Eta'] > 100), 'Eta'] = np.nan # rendo NaN i valori fuori range (es. < 18 o > 100)
    
    mediana_eta = df['Eta'].median() # calcolo la mediana della colonnna 
    df['Eta'] = df['Eta'].fillna(mediana_eta) # riempio i buchi

    # NORMALIZZAZIONE BOLLETTA UNICA
    df['Bolletta_Unica'] = df['Bolletta_Unica'].str.lower().str.strip()
    mappa_bolletta = {'sì': 'Sì', 'si': 'Sì', 'no': 'No'}
    df['Bolletta_Unica'] = df['Bolletta_Unica'].map(mappa_bolletta).fillna('No')

    # NORMALIZZAZIONE DISDETTA
    df['Disdetta'] = df['Disdetta'].fillna('No')
    
    print("Creazione fasce d'età...")
    bins = [0, 30, 50, 70, 120] #confini età
    labels = ['Giovani (<30)', 'Adulti (30-50)', 'Senior (50-70)', 'Over 70']
    df['Fascia_Eta'] = pd.cut(df['Eta'], bins=bins, labels=labels)
    
    nuovo_ordineCol = ['ID_Cliente', 'Nome', 'Eta', 'Fascia_Eta', 'Bolletta_Unica', 'Costo_Mensile_Medio', 'Disdetta']
    df = df[nuovo_ordineCol]

    # ---- FASE: ANALISI  ----
    print("\n----  FASE: ANALISI  ----\n")
    
    print("\n --- Dataframe Pulito : ---")
    print(df)

    # Calcolo percentuale Disdetta Generale
    conteggio_disdetta = df['Disdetta'].value_counts(normalize=True) * 100
    print("\nPercentuale Churn (Abbandono) Generale:")
    print(conteggio_disdetta)
    
    # Analisi Churn per tipo di servizio (Bolletta Unica)
    print("\nPercentuale Churn per Bolletta Unica:")
    churn_per_servizio = df.groupby('Bolletta_Unica')['Disdetta'].value_counts(normalize=True).unstack() * 100
    print(churn_per_servizio)
    
    # ---- FASE: ESPORTAZIONE (NUOVA) ----
    print("\nSalvataggio dei dati puliti in corso...")
    df.to_csv('ZDeposito_csv_txt/clienti_energy_cleaned.csv', index=False)
    print("File 'clienti_energy_cleaned.csv' creato con successo!")

    # ---- FASE: VISUALIZZAZIONE ----
    # figure con 3 grafici
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # 1) Grafico a Torta: Churn Generale
    colori_pie = ['#66b3ff','#ff9999']
    ax1.pie(conteggio_disdetta, labels=conteggio_disdetta.index, autopct='%1.1f%%', 
            startangle=90, colors=colori_pie, explode=(0.05, 0))
    ax1.set_title('Churn Rate Generale')

    # 2) Istogramma: Distribuzione Età
    ax2.hist(df['Eta'], bins=20, color='skyblue', edgecolor='black')
    ax2.axvline(mediana_eta, color='red', linestyle='--', label=f'Mediana: {mediana_eta}')
    ax2.set_title('Distribuzione Età (Pulita)')
    ax2.set_xlabel('Età')
    ax2.legend()

    # 3) Grafico a Barre: Churn per Bolletta Unica (IL NUOVO DATO)
    churn_per_servizio.plot(kind='bar', stacked=True, ax=ax3, color=['#66b3ff','#ff9999'])
    ax3.set_title('Impatto Bolletta Unica su Disdetta')
    ax3.set_ylabel('Percentuale %')
    ax3.set_xlabel('Ha la Bolletta Unica?')
    ax3.legend(title='Disdetta')
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()