import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df.columns = pd.Index([col.lower() for col in df.columns])

    return df
