from main.config.postgresConnection import connectAndExcecute


def getSomeAirportData(cursor):
    columns = "id, geom, gid, fna"
    tableName = "Aeropuerto"
    cursor.execute(f"SELECT {columns} FROM \"{tableName}\"")

    # Recorremos los resultados y los mostramos
    for nombre in cursor.fetchall():
        print(nombre)


def createAirportTable(cursor):
    createTableQuery = """
        create table "Airport" (
            id      serial not null primary key,
            geom    geometry(Point, 4326),
            gid     integer,
            entidad bigint,
            objeto  varchar,
            fna     varchar,
            gna     varchar,
            nam     varchar,
            fun     double precision,
            fdc     varchar,
            sag     varchar
        );
        """
    cursor.execute(createTableQuery)


if __name__ == "__main__":
    connectAndExcecute(createAirportTable)
