import sqlite3
import pandas as pd

def query_database():

    connection = sqlite3.connect("pipeline.db")

    query = """
    SELECT id, name, email
    FROM users
    """

    df = pd.read_sql_query(query, connection)

    print("\nDATABASE QUERY RESULT\n")
    print(df)

    connection.close()

if __name__ == "__main__":
    query_database()