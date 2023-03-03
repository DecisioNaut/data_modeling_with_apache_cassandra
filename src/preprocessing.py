from pathlib import Path

import pandas as pd


def preprocess_data(raw_data_path: Path) -> pd.DataFrame:
    """Preprocess data from input folder and return a dataframe."""
    dfs = []
    for file in raw_data_path.glob("*.csv"):
        df = pd.read_csv(file)
        dfs.append(df)
    return pd.concat(dfs)
