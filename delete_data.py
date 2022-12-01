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


def delete_where(conn, table, **kwargs):
    """
    Delete from table where attributes from
    :param conn: Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """

    qs = []
    values = tuple()
    for k,v in kwargs.items():
        qs.append(f"{k} = ?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f"DELETE FROM {table} WHERE {q}"
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")



if __name__ == "__main__":
    conn = create_connection("mundial.db")
    delete_where(conn, "details", id=1)