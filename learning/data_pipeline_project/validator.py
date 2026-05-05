import pandas as pd

def validate(data):
    if data is None:
        raise ValueError("Dataset is empty")

    try:
        rows = list(data)
    except TypeError:
        raise ValueError("Dataset must be iterable")

    if len(rows) == 0:
        raise ValueError("Dataset is empty")

    # Convert to DataFrame (important for pipeline)
    df = pd.DataFrame(rows)

    # Check missing values
    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values")

    # Check duplicates
    if df.duplicated().sum() > 0:
        raise ValueError("Dataset contains duplicate rows")

    return df