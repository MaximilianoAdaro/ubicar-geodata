from main.config.postgresConnection import connectAndExcecute


def createMultiPointGeomDataTable(cursor, tableName):
    createTableQuery = """
        create table if not exists {} (
            id      serial not null primary key,
            geom    geometry(MultiLineString, 4326),
            gid     integer,
            entidad bigint,
            objeto  varchar,
            fna     varchar,
            gna     varchar,
            nam     varchar,
            rgc     double precision,
            ltn     bigint,
            loc     double precision,
            fdc     varchar,
            sag     varchar
        );
        """.format(f"\"{tableName}\"")
    cursor.execute(createTableQuery)


if __name__ == "__main__":
    availableIgnLayers = ['Ferrocarril']
    for dataName in availableIgnLayers:
        connectAndExcecute(createMultiPointGeomDataTable, dataName)
