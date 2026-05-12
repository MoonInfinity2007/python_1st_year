import sys
import numpy as np


def make_board(n):
    return np.fromfunction(lambda x, y: 1 ^ ((x + y) % 2), (n, n), dtype=int)


exec(sys.stdin.read())
