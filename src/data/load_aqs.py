# src/data/load_aqs.py
import pandas as pd

def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Load raw EPA AQS data from CSV.
    """
    df = pd.read_csv(file_path)
    return df