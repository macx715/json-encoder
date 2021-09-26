import json, sys
from psycopg2 import connect, Error

valid_dst = fr'C:<>.json'

with open(valid_dst) as json_data:
    record_list = json.load(json_data)

# if type(record_list) == list:
#     first_record = record_list[0]
#     columns = list(first_record.keys())
#     print("\ncolumn name:", columns)

columns = [list(x.keys()) for x in record_list][0]
print("\ncolumn name:", columns)

table_name = 'logins'
sql_string = 'INSERT INTO security.{} '.format(table_name)
sql_string += "(" + ', '.join(columns) + ")\nVALUES "

values = [list(x.values()) for x in record_list]
print(values)

for i, record_dict in enumerate(record_list):
    values = []
    for col_names, val in record_dict.items():
        if type(val) == str:
            val = val.replace("'", "''")
            val = "'" + val + "'"
        values += [str(val)]
    sql_string += "(" + ', '.join(values) + "),\n"

sql_string = sql_string[:-2] + ";"
print("\nSQL statement:")
print(sql_string)

# connection and insert data
try:
    conn = connect(
        dbname='<>>',
        user='postgres',
        host='localhost',
        password='password',
        connect_timeout='3',
    )
    cur = conn.cursor()
    print("\ncreated cursor object:", cur)
except (Exception, Error) as err:
    print("\npsycopg2 connection error:", err)
    conn = None
    cur = None

if cur != None:
    try:
        #cur.execute(sql_string)
        conn.commit()
        print('\nfinished INSERT INTO execution')
    except (Exception, Error) as error:
        print("\nexecute_sql () error:", error)
        conn.rollback()

    cur.close()
    conn.close()
