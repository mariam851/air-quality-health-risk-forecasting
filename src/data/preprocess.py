# src/data/preprocess.py

import pandas as pd

def preprocess_aqs_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess raw air quality data.
    """
    # Rename columns
    df = df.rename(columns={
        "StateFips": "state_fips",
        "StateName": "state",
        "CountyFips": "county_fips",
        "CountyName": "county",
        "ReportYear": "year",
        "MeasureId": "measure_id",
        "MeasureName": "measure_name",
        "Value": "value",
        "DataOrigin": "data_origin",
        "MonitorOnly": "monitor_only"
    })

    # Convert types
    df["year"] = df["year"].astype(int)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["monitor_only"] = df["monitor_only"].astype(bool)

    # Missing value indicator
    df["value_missing"] = df["value"].isna().astype(int)

    # Sort
    df = df.sort_values(["state_fips", "county_fips", "year"])

    # Lag features
    df["value_lag_1"] = df.groupby(["state_fips", "county_fips"])["value"].shift(1)
    df["value_lag_3"] = df.groupby(["state_fips", "county_fips"])["value"].shift(3)

    # Rolling mean
    df["rolling_mean_3"] = df.groupby(["state_fips", "county_fips"])["value"].transform(lambda x: x.rolling(3).mean())

    # Normalized year
    df["year_norm"] = df["year"] - df["year"].min()

    # High-risk flag
    df["high_risk"] = (df["value"] > df["value"].quantile(0.75)).astype(int)

    return df