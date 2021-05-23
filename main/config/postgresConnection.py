import psycopg2

from main.config.config import config


def connectAndExcecute(excecuteFunction, tableName):
    """Connect to the PostgreSQL database server"""
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        # create a cursor
        cursor = connection.cursor()

        # Ejecutamos una consulta
        excecuteFunction(cursor, tableName)

        # close the communication with the PostgreSQL
        cursor.close()

        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
