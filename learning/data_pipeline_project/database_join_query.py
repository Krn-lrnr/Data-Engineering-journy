import sqlite3
import pandas as pd

def join_query():

    connection = sqlite3.connect("pipeline.db")

    query = """
    SELECT
        users.id,
        users.name,
        contacts.email,
        contacts.phone,
        contacts.website
    FROM users
    JOIN contacts
    ON users.id = contacts.id
    """

    df = pd.read_sql_query(query, connection)

    print("\nJOIN QUERY RESULT\n")
    print(df)

    connection.close()

if __name__ == "__main__":
    join_query()