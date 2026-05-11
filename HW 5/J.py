import sys
import pandas as pd


def best(data):
    mask = (data['maths'] >= 4) & (data['physics'] >= 4) & (data['computer science'] >= 4)
    return data[mask]


exec(sys.stdin.read())
