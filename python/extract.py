import pandas as pd


def extract_csv(file_path):

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} rows from {file_path}")

    return df