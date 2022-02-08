import os
import json
import geojson
import definitions as definitions
from main.manageData.geoEspatialData.databaseTable.manageComonUseges import deleteAllNotAppearingInNewData
from main.runAll import FOLDER_NAME


def importPointGeomData(cursor, tableName):
    with open(os.path.join(definitions.OUTPUT_PATH, FOLDER_NAME, f"{tableName}.json")) as file:
        gj = geojson.load(file)
    allGId = []
    for feature in gj['features']:
        properties_ = feature['properties']
        geom = (json.dumps(feature['geometry']))
        gid = properties_['gid']
        allGId.append(gid)
        station = properties_['station']
        line = properties_['line']

        if (station is not None) & (line is not None):
            cursor.execute(
                f"""
                INSERT INTO \"{tableName}\"
                (geom, gid, station, line) 
                VALUES 
                (ST_GeomFromText(ST_AsText(ST_GeomFromGeoJSON(%s))), %s, %s, %s)
                on conflict (gid) do update set
                            (geom, station, line) =
                            (EXCLUDED.geom, EXCLUDED.station, EXCLUDED.line)
                """,
                (geom, gid, station, line,)
            )

    deleteAllNotAppearingInNewData(allGId, cursor, tableName)

