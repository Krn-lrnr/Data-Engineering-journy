import pandas as pd

def validate(data):
    df = pd.DataFrame(data)

    # check empty dataset
    if df.empty:
        raise ValueError("Dataset is empty")

    # check missing values
    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values")

    # check duplicates
    if df.duplicated().sum() > 0:
        raise ValueError("Dataset contains duplicate rows")

    return df