#questo file è stato fatto solo per visualizzare su una mappa tutte le coordinate
import pandas as pd


path = "data_files/Brightkite_totalCheckins.txt"
df = pd.read_table(path, delimiter='\t', names=['source', 'date', 'lat', 'lon', 'hash'])
print(df.head()[['lon', 'lat']])
with open('all_coordinates.txt', 'w') as f:
    for index, row in df.iterrows():
        f.write(f"{row['lon']}\t{row['lat']}\n")