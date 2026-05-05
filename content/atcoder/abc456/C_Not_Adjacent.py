s = input()
n = len(s)
left = 0

ans = 0

while left  < n:
    right = left
    while right + 1 < n and s[right] != s[right + 1]:
        right += 1

    # print(s[left : right], "is valid")
    L = right - left + 1
    ans += (L)*(L + 1) // 2
    left = right + 1

print(ans % 998244353)
