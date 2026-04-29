H, W = map(int, input().split())

s = list()
for i in range(H):
    temp = list(input())
    s.append(temp)

# print(*s, sep = '\n')

ans = 0

for h1 in range(H):
    for w1 in range(W):
        for h2 in range(h1, H):
            for w2 in range(w1, W):
                #print(h1, w1, h2, w2)
                flag = 0
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if s[h1 + h2 - i][w1 + w2 - j] == s[i][j]:
                            pass
                        else:
                            flag = 1
                if flag == 0:
                    ans += 1

print(ans)

