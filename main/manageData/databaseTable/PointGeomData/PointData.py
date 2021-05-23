from main.config.postgresConnection import connectAndExcecute


def createPointGeomDataTable(cursor, tableName):
    createTableQuery = """
        create table if not exists {} (
            id      serial not null primary key,
            geom    geometry(Point, 4326),
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
    availableIgnLayers = ['Cuartel de bomberos', 'Institución penitenciaria', 'Edificio de seguridad',
                          'Establecimiento educativo', 'Edificio de salud', 'Estación de ferrocarril', 'Puerto',
                          'Universidad']
    for dataName in availableIgnLayers:
        connectAndExcecute(createPointGeomDataTable, dataName)
