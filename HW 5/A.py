import sys
import numpy as np


def multiplication_matrix(n):
    return np.fromfunction(lambda x, y: (x + 1) * (y + 1), (n, n), dtype=int)


exec(sys.stdin.read())
