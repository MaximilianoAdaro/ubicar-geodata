def createCityGeomDataTable(cursor, tableName):
    createTableQuery = """
        create table if not exists {} (
            id         serial not null primary key,
            gid        double precision unique,
            name       varchar not null,
            state_id   varchar
        );
        """.format(f"\"{tableName}\"")
    cursor.execute(createTableQuery)


if __name__ == "__main__":
    from main.config.postgresConnection import connectAndExcecute
    connectAndExcecute(createCityGeomDataTable, 'city')
