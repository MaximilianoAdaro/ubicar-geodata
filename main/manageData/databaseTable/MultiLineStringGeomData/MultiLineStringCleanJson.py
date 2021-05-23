import json

import geojson
from main.config.postgresConnection import connectAndExcecute


def importMultiPointGeomData(cursor, tableName):
    with open("/home/maxi/projects/ubicar/ubicar-geodata/output/geojsonData2/{}.json".format(tableName)) as file:
        gj = geojson.load(file)
    for feature in gj['features']:
        properties_ = feature['properties']
        geom = (json.dumps(feature['geometry']))
        gid = properties_['gid']
        entidad = properties_['entidad']
        objeto = properties_['objeto']
        fna = properties_['fna']
        gna = properties_['gna']
        nam = properties_['nam']
        ltn = properties_['ltn']
        loc = properties_['loc']
        fdc = properties_['fdc']
        sag = properties_['sag']

        if (fna is not None) & (nam is not None):
            cursor.execute(
                """
                INSERT INTO {}
                (geom, gid, entidad, objeto, fna, gna, nam, ltn, loc, fdc, sag) 
                VALUES 
                (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))),%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """.format(f"\"{tableName}\""),
                (geom, gid, entidad, objeto, fna, gna, nam, ltn, loc, fdc, sag,)
            )


if __name__ == "__main__":
    availableIgnLayers = ['Ferrocarril']
    for dataName in availableIgnLayers:
        connectAndExcecute(importMultiPointGeomData, dataName)
