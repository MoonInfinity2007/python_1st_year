import sys
import numpy as np


def get_det_matrix(a):
    return np.linalg.det(a)


exec(sys.stdin.read())
