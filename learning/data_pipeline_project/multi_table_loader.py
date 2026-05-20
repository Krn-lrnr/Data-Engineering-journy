import sqlite3
import pandas as pd

def load_multiple_tables(df):

    connection = sqlite3.connect("pipeline.db")

    users_df = df[["id", "name"]]

    contacts_df = df[["id", "email", "phone", "website"]]

    users_df.to_sql(
        "users",
        connection,
        if_exists="replace",
        index=False
    )

    contacts_df.to_sql(
        "contacts",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Data loaded into multiple tables successfully")