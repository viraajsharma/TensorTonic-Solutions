import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    n,m = len(A),len(A[0])
    result = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            result[j][i] = A[i][j]
    return result