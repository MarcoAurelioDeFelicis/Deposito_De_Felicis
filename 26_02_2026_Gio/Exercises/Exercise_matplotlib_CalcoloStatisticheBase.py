import pandas as pd
import numpy as np

np.random.seed(42)
temperature_data = np.random.uniform(15, 30, size=30)

# DataFrame
df = pd.DataFrame(temperature_data, columns=['temperature'])

print("Prime 5 righe del dataset:")
print(df.head())
# print(df)
print("dimensione Dataset: ",len(df))

print("\n\n --- Calcolo delle Statistiche ---\n")
massima = df['temperature'].max()
minima = df['temperature'].min()
media = df['temperature'].mean()
mediana = df['temperature'].median()

print("-" * 30)
print(f"REPORT TEMPERATURE MENSILI")
print("-" * 30)
print(f"Temperatura Massima:  {massima:.2f}°C")
print(f"Temperatura Minima:   {minima:.2f}°C")
print(f"Temperatura Media:    {media:.2f}°C")
print(f"Mediana:              {mediana:.2f}°C")
print("-" * 30)

print(df['temperature'].describe().round(2))

# --------- VISUALIZZAZIONE -------------------------

import matplotlib.pyplot as plt

# stile grafico
plt.style.use('seaborn-v0_8') # o 'ggplot'

# figura
plt.figure(figsize=(10, 6))

# plot della serie temporale (le temperature giornaliere)
plt.plot(df.index + 1, df['temperature'], marker='o', linestyle='-', color='royalblue', label='Temp. Giornaliera')

# aggiunta delle linee statistiche (Orizzontali)
# axhline per tracciare linee che attraversano tutto il grafico
plt.axhline(media, color='green', linestyle='--', linewidth=1.5, label=f'Media: {media:.2f}°C')
plt.axhline(massima, color='red', linestyle=':', linewidth=1.5, label=f'Massima: {massima:.2f}°C')
plt.axhline(minima, color='orange', linestyle=':', linewidth=1.5, label=f'Minima: {minima:.2f}°C')

#personalizzazione degli assi e dei titoli
plt.title('Andamento delle Temperature Mensili', fontsize=14, fontweight='bold')
plt.xlabel('Giorno del Mese', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.xticks(range(1, len(df)+1)) # Mostra tutti i giorni sull'asse X
plt.grid(True, alpha=0.3)# stile background
plt.legend() # Mostra la legenda con le etichette definite

# mostra  grafico
plt.tight_layout() #adatta il grafico alla finestra
plt.show()