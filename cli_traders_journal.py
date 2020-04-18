import psycopg2
import config
import click



import@click.command()
@click.option('--instrument', prompt='Instrument',
              help='The instrument used in trade')
def insert_in_db(instrument):
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="trading_journal",
            user="masha",
            host="127.0.0.1",
            password="trading",
            port="5432"
        )
        # create a new cursor
        cur = conn.cursor()
        sql = """ INSERT INTO journal(instrument) VALUES(%s)"""
        variables = (instrument)
        # execute the INSERT statement
        cur.execute(sql, variables)
        # commit the changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into journal")
    except (Exception, psycopg2.Error) as error:
        if (conn):
            print("Failed to insert record into journal", error)
    finally:
            # closing database connection.
        if (conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

    return instrument


if __name__ == '__main__':
    insert_in_db()