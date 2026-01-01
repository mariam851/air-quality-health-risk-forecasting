# src/features/build_features.py

def get_features():
    """
    Return list of feature columns for modeling.
    """
    return ["value_lag_1", "value_lag_3", "rolling_mean_3", "year_norm"]

def get_target():
    """
    Return the target column for prediction.
    """
    return "value"
