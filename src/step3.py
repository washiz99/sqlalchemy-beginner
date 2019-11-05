"""
step3: insert/update/delete
"""
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# insert statement
ins_stat = """
    INSERT INTO city
        (Name, CountryCode, District, Population)
    VALUES
        (:name, :countryCode, :district, :population)
"""

# update statement
upd_stat = """
    UPDATE city SET population = :Population WHERE ID = :id;
"""

# delete statement
del_stat = """
    DELETE FROM city WHERE ID = :id;
"""


# connect database
conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
e = create_engine(conn_string)

# execute insert statement
e.execute(text(ins_stat), name='Hannan', countryCode='JPN', district='Osaka', population=51747)

result = e.execute("SELECT * FROM city WHERE Name = 'Hannan';")
row = result.fetchone()
pkey = row.ID
print(row)

# execute update statement
e.execute(text(upd_stat), Population=56789, id=pkey)

result = e.execute("SELECT * FROM city WHERE Name = 'Hannan';")
row = result.fetchone()
print(row)

# execute delete statement
e.execute(text(del_stat), id=pkey)

result = e.execute("SELECT * FROM city WHERE Name = 'Hannan';")
row = result.fetchone()
print(row)
