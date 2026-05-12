import sys
import numpy as np


def rotate(a, ang):
    return np.rot90(a, k=ang//90, axes=(1,0))


exec(sys.stdin.read())
