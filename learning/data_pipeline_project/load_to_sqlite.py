import sqlite3

def load_to_sqlite(df, database_name="pipeline.db", table_name="users"):

    connection = sqlite3.connect(database_name)

    df.to_sql(table_name, connection, if_exists="replace", index=False)

    connection.close()

    print(f"Data loaded into SQLite database: {database_name}")