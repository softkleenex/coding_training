t, x = map(int, input().split())
a = list(map(int, input().split()))
pev = a[0]
print(0, a[0])
for i in range(len(a)):
    if abs(a[i] - pev) >= x:
        print(i, a[i])
        pev = a[i]
