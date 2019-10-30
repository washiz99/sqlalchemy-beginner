"""
step2: query parameter
"""
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# connect database
conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
e = create_engine(conn_string)

# In pymysql, '%s' is used as a placeholder for query parameter.
query = 'select * from city where CountryCode = %s and Population >= %s;'
# Both integer and strins can be used.
result = e.execute(query, 'JPN', 1000000)
for row in result:
    print(row)

# use :valiable
query2 = 'select * from city where CountryCode = :countryCode and Population >= :population;'
result2 = e.execute(text(query2), countryCode='USA', population=1000000)
for row2 in result2:
    print(row2)
