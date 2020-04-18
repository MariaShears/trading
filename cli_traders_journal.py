import click
import sqlite3

@click.command()
@click.option('--instrument', prompt='Instrument',
              help='The instrument used in trade')
def insert_in_db(instrument):

    try:
        sqliteConnection = sqlite3.connect('traders_journal.db')
        cursor = sqliteConnection.cursor()
        variables = (instrument,)
        sql = '''INSERT INTO journal(instrument) VALUES(?)'''
        cursor.execute(sql, variables)
        sqliteConnection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into journal")
    except sqlite3.Error as error:
        print("Failed to insert record into journal", error)
    finally:
        if (sqliteConnection):
            cursor.close()
            sqliteConnection.close()
            print("The SQLite connection is closed")


if __name__ == '__main__':
    insert_in_db()