from collections import *

n, m = map(int, input().split())
fri = list()
fg = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in fg.keys():
        fg[a].append(b)
    else:
        fg[a] = [b]

# print(fg)
item = [1]
ans = set([1])


while len(item) > 0:
    curr = item.pop()
    if curr in fg.keys():
        for v in fg[curr]:
            if v in ans:
                pass
            else:
                ans.add(v)
                item.append(v)

print(len(ans))
