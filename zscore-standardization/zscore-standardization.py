import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    X_arr = np.asarray(X, dtype=float)
    mean = np.mean(X_arr, axis=axis, keepdims=True)
    std = np.std(X_arr, axis=axis, keepdims=True)
    
    is_valid = std > eps
    safe_std = np.where(is_valid, std, 1.0)
    
    return np.where(is_valid, (X_arr - mean) / safe_std, 0.0)