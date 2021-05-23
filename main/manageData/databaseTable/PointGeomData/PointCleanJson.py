import json

import geojson
from main.config.postgresConnection import connectAndExcecute


def importPointGeomData(cursor, tableName):
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
        fdc = properties_['fdc']
        sag = properties_['sag']

        if (fna is not None) & (nam is not None):
            cursor.execute(
                """
                INSERT INTO {}
                (geom, gid, entidad, objeto, fna, gna, nam, fdc, sag) 
                VALUES 
                (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))), %s, %s, %s, %s, %s, %s, %s, %s)
                """.format(f"\"{tableName}\""),
                (geom, gid, entidad, objeto, fna, gna, nam, fdc, sag,)
            )


if __name__ == "__main__":
    availableIgnLayers = ['Cuartel de bomberos', 'Institución penitenciaria', 'Edificio de seguridad',
                          'Establecimiento educativo', 'Edificio de salud', 'Estación de ferrocarril', 'Puerto',
                          'Universidad']
    for dataName in availableIgnLayers:
        connectAndExcecute(importPointGeomData, dataName)
