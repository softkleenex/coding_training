# https://www.acmicpc.net/problem/1895
from sys import stdin
input = stdin.readline


r, c = map(int, input().split())

datas = [list(map(int, input().split())) for x in range(r) ]

# print(*datas, sep = '\n')



pos = ((+1, +1), (+1, 0), (+1, -1), (0, +1), (0, 0), (0, -1), (-1, +1), (-1, 0), (-1, -1))

datastemp =  []

for (r) in range((1), len(datas)-1):
    templ = []
    for (c) in range(1, len(datas[0])-1):
        temp = []
        for temppos in pos:
            temp.append(datas[r + int(temppos[0])][c + int(temppos[1])])
            
        temp.sort()
        templ.append(temp[4])
    datastemp.append(templ)

    
# print(*datastemp, sep = '\n')

c = 0
t = int(input())
for x in datastemp:
    for x2 in x:
        c += 1 if x2 >= t else 0
    
print(c)