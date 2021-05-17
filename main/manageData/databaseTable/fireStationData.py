from main.config.postgresConnection import connectAndExcecute


def createFireStationTable(cursor):
    createTableQuery = """
        create table "Fire Station" (
            id      serial not null primary key,
            geom    geometry(Point, 4326),
            gid     integer,
            entidad bigint,
            objeto  varchar,
            fna     varchar,
            gna     varchar,
            nam     varchar,
            tes     double precision,
            fdc     varchar,
            sag     varchar
        );
        """
    cursor.execute(createTableQuery)


if __name__ == "__main__":
    connectAndExcecute(createFireStationTable)
