import sys
import pandas as pd


def cheque(data, **kwargs):
    rows = []
    for product, number in kwargs.items():
        price = data[product]
        rows.append([product, price, number, price * number])
    df = pd.DataFrame(rows, columns=['product', 'price', 'number', 'cost'])
    df = df.sort_values(by='product').reset_index(drop=True)
    return df


exec(sys.stdin.read())
