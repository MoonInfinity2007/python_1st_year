def C(n, k):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)


n = int(input())
k = int(input())
print(C(n))
