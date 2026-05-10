import pandas as pd
from transform import transform

def test_transform():
    sample_data = [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com"
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com"
        }
    ]

    df = transform(sample_data)

    assert isinstance(df, pd.DataFrame)

    assert list(df.columns) == ["id", "name", "email"]

    assert len(df) == 2

    print("All tests passed")

if __name__ == "__main__":
    test_transform()