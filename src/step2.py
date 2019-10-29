"""
step1: execute query
"""
from sqlalchemy import create_engine

# connect database
conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
e = create_engine(conn_string)

# In pymysql, '%s' is used as a placeholder for query parameter.
query = 'select * from city where CountryCode = %s and Population >= %s;'
# Both integer and strins can be used.
result = e.execute(query, 'JPN', 1000000)

for row in result:
    print(row)
