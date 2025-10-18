import numpy as np

def rmse_xy(pred_xy: np.ndarray, true_xy: np.ndarray) -> float:
    """Root mean squared error for (x,y) arrays of shape (N,2)."""
    return float(np.sqrt(np.mean((pred_xy - true_xy) ** 2)))
