import psycopg2
from configparser import ConfigParser

#https://www.postgresqltutorial.com/postgresql-python/connect/

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    """Connection to the postgresql database server"""

    conn = None

    try:
        # read connection parameters
        params = config()

        # connect to the postgresql server
        print('connecting to the postgresql database...')
        conn = psycopg2.connect(**params)

        # create cursor
        cur = conn.cursor()

        # execute statement
        print('PostgresSQL database version:')
        cur.execute('select version()')

        # display the postrgresql database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the postgresql
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('database connection close')


if __name__ == '__main__':
    connect()
