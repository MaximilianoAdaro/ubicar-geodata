import os

import geojson

import definitions as definitions
from main.runGeoRef import FOLDER_NAME


def importStateGeomData(cursor, tableName):
    with open(os.path.join(definitions.OUTPUT_PATH, FOLDER_NAME, f"{tableName}.json")) as file:
        gj = geojson.load(file)
    for feature in gj['features']:
        properties_ = feature['properties']
        gid = properties_['id']
        name = properties_['nombre']

        if name is not None:
            cursor.execute(
                f"""
                INSERT INTO \"{tableName}\"
                (gid, name) 
                VALUES 
                (%s, %s)
                """,
                (gid, name,)
            )


if __name__ == "__main__":
    from main.config.postgresConnection import connectAndExcecute

    connectAndExcecute(importStateGeomData, 'state')
