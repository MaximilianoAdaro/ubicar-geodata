import os
import json
import geojson
import definitions as definitions
from main.runGeoRef import FOLDER_NAME


def importCityGeomData(cursor, tableName):
    with open(os.path.join(definitions.OUTPUT_PATH, FOLDER_NAME, f"{tableName}.json")) as file:
        gj = geojson.load(file)
    for feature in gj['features']:
        properties_ = feature['properties']
        geom = (json.dumps(feature['geometry']))
        gid = properties_['id']
        name = properties_['nombre']
        state = properties_['provincia']['id']

        if (state is not None) & (name is not None):
            cursor.execute(
                f"""
                INSERT INTO \"{tableName}\"
                (geom, gid, name, state_id)
                VALUES 
                (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))), %s, %s, %s)
                """,
                (geom, gid, name, state,)
            )


if __name__ == "__main__":
    from main.config.postgresConnection import connectAndExcecute
    connectAndExcecute(importCityGeomData, 'city')
