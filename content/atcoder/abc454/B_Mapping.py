N, M = map(int, input().split())
F = list(map(int, input().split()))

print("Yes") if len(F) == len(set(F)) else print("No")

flag = 0
for v in range(1, M + 1):
    if not(v in F):
        flag = 1

print("Yes") if flag == 0 else print("No")
