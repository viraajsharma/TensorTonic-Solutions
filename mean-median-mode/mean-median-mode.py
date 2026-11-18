from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    mode = counts.most_common(1)[0][0]
    return {"mean" : float(mean) , "median": float(median) , "mode": float(mode)}