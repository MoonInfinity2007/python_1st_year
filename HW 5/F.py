import sys
import pandas as pd
import re


def length_stats(s):
    s = re.sub(r'[^\w\s]|[\d]', '', s)
    s = s.lower().split()
    data_o = {}
    data_e = {}
    for i in range(len(s)):
        if (len(s[i]) % 2):
            data_o[s[i]] = len(s[i])
        else:
            data_e[s[i]] = len(s[i])
    odd = pd.Series(data_o, dtype='int64')
    odd = odd.sort_index()
    even = pd.Series(data_e, dtype='int64')
    even = even.sort_index()
    return (odd, even)


exec(sys.stdin.read())
