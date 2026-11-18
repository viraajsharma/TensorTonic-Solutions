import numpy as np

def sample_var_std(x: list) -> dict:
    return {'variance': float(np.var(x,ddof = 1)) , 'standard_deviation': float(np.std(x,ddof = 1))}