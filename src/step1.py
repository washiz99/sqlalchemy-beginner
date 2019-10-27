"""
step1: execute query
"""
from sqlalchemy import create_engine

# connect database
conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
e = create_engine(conn_string)

result = e.execute('select * from city limit 10;')

# access result (The return value type is ResultProxy defined by sqlalchemy.)
for row in result:
    print('---')
    print(row)
    # access via integer position.
    print(row[1])
    # access via name like a attribute.
    print(row.District)
    # access via column name.
    print(row['Population'])
