from main.config.postgresConnection import connectAndExcecute


def createMultiPolygonGeomDataTable(cursor, tableName):
    createTableQuery = """
        create table if not exists {} (
            id      serial not null primary key,
            geom    geometry(MultiPolygon, 4326),
            gid     integer,
            entidad bigint,
            objeto  varchar,
            fna     varchar,
            gna     varchar,
            nam     varchar,
            fdc     varchar,
            sag     varchar
        );
        """.format(f"\"{tableName}\"")
    cursor.execute(createTableQuery)


if __name__ == "__main__":
    availableIgnLayers = ['Área de fabricación y procesamiento']
    for dataName in availableIgnLayers:
        connectAndExcecute(createMultiPolygonGeomDataTable, dataName)
