from sqlalchemy import create_engine


def main():
    # connect database
    conn_string = 'mysql+pymysql://root:mysql@127.0.0.1:3306/world'
    engine = create_engine(conn_string)

    query = 'select * from city limit 10;'
    result = engine.execute(query)

    for row in result:
        print(row)


if __name__ == '__main__':
    main()
