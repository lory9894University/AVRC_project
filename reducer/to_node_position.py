import pandas as pd
import json

if __name__ == '__main__':
    path = "../data_files/Brightkite_totalCheckins.txt"
    df = pd.read_table(path, delimiter='\t', names=['source', 'date', 'lat', 'lon', 'hash'])
    df.drop(['date'], axis=1, inplace=True)
    df = df.set_index('source')
    df = df.groupby('source').hash.agg(lambda x: x.mode()[0])
    df.to_json('../data_files/node_estimate_coord.json',orient='index')