a = list(map(int, input().split()))
k = 0
for i in range(len(a)):
    if (a[i] != 0):
        a[k], a[i] = a[i], a[k]
        k += 1
print(*a)