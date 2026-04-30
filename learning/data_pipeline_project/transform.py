import pandas as pd

def transform(data):
    df = pd.DataFrame(data)
    df = df[["id", "name", "email"]]
    df = df.dropna()
    return df