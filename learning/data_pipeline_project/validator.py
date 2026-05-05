def validate(data):
    if data is None:
        raise ValueError("Dataset is empty")

    try:
        rows = list(data)
    except TypeError:
        raise ValueError("Dataset must be iterable")

    if len(rows) == 0:
        raise ValueError("Dataset is empty")

    for row in rows:
        if row is None:
            raise ValueError("Dataset contains missing values")

        if isinstance(row, dict):
            if any(value is None for value in row.values()):
                raise ValueError("Dataset contains missing values")
        elif isinstance(row, (list, tuple, set)):
            if any(value is None for value in row):
                raise ValueError("Dataset contains missing values")

    seen = set()
    for row in rows:
        if row in seen:
            raise ValueError("Dataset contains duplicate rows")
        seen.add(row)

    return rows