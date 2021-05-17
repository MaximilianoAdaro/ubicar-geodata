import json

import geojson
from main.config.postgresConnection import connectAndExcecute


def getSomeAirportData(cursor):
    columns = "id, geom, gid, fna"
    tableName = "Aeropuerto"
    cursor.execute(f"SELECT {columns} FROM \"{tableName}\"")

    # Recorremos los resultados y los mostramos
    for nombre in cursor.fetchall():
        print(nombre)


def insertAirpotData(cursor):
    with open("../../../output/geojsonData2/Aeropuerto.json") as file:
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
        fun = properties_['fun']
        fdc = properties_['fdc']
        sag = properties_['sag']

        cursor.execute(
            """
            INSERT INTO "Airport" 
            (geom, gid, entidad, objeto, fna, gna, nam, fun, fdc, sag) 
            VALUES 
            (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))), %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (geom, gid, entidad, objeto, fna, gna, nam, fun, fdc, sag,)
        )


if __name__ == "__main__":
    connectAndExcecute(insertAirpotData)
