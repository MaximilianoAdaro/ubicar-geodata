import os
import json
import geojson
import definitions as definitions
from main.manageData.geoEspatialData.databaseTable.manageComonUseges import deleteAllNotAppearingInNewData
from main.runAll import FOLDER_NAME


def importMultiPolygonGeomData(cursor, tableName):
    with open(os.path.join(definitions.OUTPUT_PATH, FOLDER_NAME, f"{tableName}.json")) as file:
        gj = geojson.load(file)
    allGId = []
    for feature in gj['features']:
        properties_ = feature['properties']
        geom = (json.dumps(feature['geometry']))
        gid = properties_['gid']
        allGId.append(gid)
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
                (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))),%s, %s, %s, %s, %s, %s, %s, %s)
                on conflict (gid) do update set
                (geom, entidad, objeto, fna, gna, nam, fdc, sag) = 
                (EXCLUDED.geom, EXCLUDED.entidad, EXCLUDED.objeto, EXCLUDED.fna, EXCLUDED.gna, EXCLUDED.nam, 
                EXCLUDED.fdc, EXCLUDED.sag)
                """.format(f"\"{tableName}\""),
                (geom, gid, entidad, objeto, fna, gna, nam, fdc, sag,)
            )
    deleteAllNotAppearingInNewData(allGId, cursor, tableName)


if __name__ == "__main__":
    from main.config.postgresConnection import connectAndExcecute

    availableIgnLayers = ['Área de fabricación y procesamiento']
    for dataName in availableIgnLayers:
        connectAndExcecute(importMultiPolygonGeomData, dataName)
