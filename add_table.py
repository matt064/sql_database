import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to a SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return conn

def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


if __name__ == "__main__":

    create_mundials_sql = """
    -- mundial table
    CREATE TABLE IF NOT EXISTS mundials (
        id integer PRIMARY KEY,
        rok integer NOT NULL,
        zwyciezca text NOT NULL, 
        liczba_druzyn integer NOT NULL
    );      
    """
    create_details_sql = """
    -- szczegóły table
    CREATE TABLE IF NOT EXISTS details (
        id integer PRIMARY KEY,
        mundial_id integer NOT NULL,
        organizator VARCHAR(150) NOT NULL,
        otwarcie text NOT NULL,
        zamkniecie text NOT NULL,
        FOREIGN KEY (mundial_id) REFERENCES mundial (id)
    );
    """
    db_file = "mundial.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_mundials_sql)
        execute_sql(conn, create_details_sql)
        conn.close()