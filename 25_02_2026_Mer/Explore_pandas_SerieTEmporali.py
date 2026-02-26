# Serie Temporali

# Pandas offre strumenti specifici per manipolare date e
# tempi, permettendo di analizzare serie temporali, cambiare
# la frequenza dei dati, e generare periodi di tempo.

import pandas as pd
import numpy as np

# DataFrame esempio:
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', 'David'],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Vendite': [100, 150, 200, 130, 180, 210, 190] # Aggiunto per rendere utile il resample
}
df = pd.DataFrame(data)

#Converte un indice o una colonna in formato datetime, permettendo di sfruttare
# tutte le funzionalità di time series DI python

# esempio: colonna “date” in stringhe → datetime
#df['Data'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Generazione di una serie di date (stessa lunghezza del DataFrame)
# 'ME' sta per Month End (fine mese)
df['Data'] = pd.date_range(start='2021-01-01', periods=len(df), freq='ME')

# Trasformiamo la colonna in indice (Fondamentale per le Time Series)
df.set_index('Data', inplace=True)

# Resampling dei dati di una serie temporale
# Calcoliamo la media delle vendite per trimestre ('QE' = Quarter End)
df_resampled = df['Vendite'].resample('QE').mean()

print(df_resampled)




