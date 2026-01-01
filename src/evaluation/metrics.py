# src/evaluation/metrics.py
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

def evaluate_regression(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return {"r2": r2, "rmse": rmse}
