def createPointGeomDataTable(cursor, tableName):
    createTableQuery = """
        create table if not exists {} (
            id      serial not null primary key,
            geom    geometry(Point, 4326),
            gid     integer unique,
            station     varchar,
            line     varchar
        );
        """.format(f"\"{tableName}\"")
    cursor.execute(createTableQuery)
