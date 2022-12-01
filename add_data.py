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

def add_mundial(conn, mundial):
   """
   Create a new record into the mundials table
   :param conn:
   :param mundial:
   :return: mundial id
   """
   sql = '''INSERT INTO mundials(rok, zwyciezca, liczba_druzyn)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, mundial)
   conn.commit()
   return cur.lastrowid


def add_detail(conn, detail):
   """
   Create a new record into the details table
   :param conn:
   :param detail:
   :return: detail id
   """
   sql = '''INSERT INTO details(mundial_id, organizator, otwarcie, zamkniecie)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, detail)
   conn.commit()
   return cur.lastrowid


if __name__ == "__main__":

    db_file = "mundial.db"

    conn = create_connection(db_file)
    mundial = ("2018", "Francja", "32")
    m_id = add_mundial(conn, mundial)
    detail = (m_id, "Rosja", "14-06-2018", "15-07-2018")
    d_id = add_detail(conn, detail)
    conn.commit()

