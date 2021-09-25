import psycopg2
from configparser import ConfigParser
import json

# https://www.postgresqltutorial.com/postgresql-python/connect/

dst = 'C:/<path>/credsw.json'


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

    global result_set
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
        # cur.execute('select version()')
        cur.execute('select * from security.logins')

        # display the postrgresql database server version
        rows = cur.fetchall()

        result_set = []
        for row in rows:
            record = {}
            #print(type(row))
            if row:
                record['id'] = row[0]
                record['username'] = row[1]
                record['password'] = row[2]
                record['url'] = row[3]
                result_set.append(record)

        # close the communication with the postgresql
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('database connection close')

    with open(dst, 'w') as json_file: #print output to json file
        json.dump(result_set, json_file, indent=4)


if __name__ == '__main__':
    connect()
