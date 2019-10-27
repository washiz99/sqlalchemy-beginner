"""
step2: insert/update/delete
"""
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# connect database
conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
e = create_engine(conn_string)

statement = """
    insert into city
        (Name, CountryCode, District, Population)
    values
        (:name, :countryCode, :district, :population)
"""

e.execute(text(statement), name='Namagahama', countryCode='JPN', district='Shiga', population=126587)
