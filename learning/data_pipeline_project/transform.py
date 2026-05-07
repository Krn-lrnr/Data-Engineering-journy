import pandas as pd
from utils import clean_columns, remove_missing

def transform(data):
    df = pd.DataFrame(data)

    df = clean_columns(df)

    df = df[["id", "name", "email"]]

    df = remove_missing(df)

    return df