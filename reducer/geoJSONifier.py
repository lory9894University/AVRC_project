import pandas as pd
import json


def hash_to_coordinates(dataframe):
    dataframe = dataframe[['lat', 'lon', 'hash']]
    dataframe = dataframe.drop_duplicates(subset=['hash']).reset_index(drop=True)
    dict = dataframe.set_index('hash').T.to_dict('list')
    return dict


if __name__ == '__main__':
    path = "./Brightkite_totalCheckins.txt"
    df = pd.read_table(path, delimiter='\t', names=['source', 'date', 'lat', 'lon', 'hash'])
    with open("../data_files/all_datas.json") as f:
        data = json.load(f)
    hashes = hash_to_coordinates(df)
    for link in data['links']:
        link['lat'] = hashes[link['position']][0]
        link['lon'] = hashes[link['position']][1]

    geojs = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["lon"], d["lat"]],
                },
                "properties": d,

            } for d in data['links']
        ]
    }

    with open("../data_files/dataset_coord.geojson", "w", encoding="utf-8") as output_file:
        json.dump(geojs, output_file)
