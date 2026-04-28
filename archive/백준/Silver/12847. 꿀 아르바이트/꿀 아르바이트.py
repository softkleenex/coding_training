# https://www.acmicpc.net/problem/12847
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

moneys = list(map(int, input().split()))
max_moneys = sum(moneys[0: m])

pre_moneys = sum(moneys[0: m])

for i in range(1, len(moneys) - m + 1):
    #print(moneys[i : i + m ],  sum(moneys[i : i + m]))
    #max_moneys = max(max_moneys, sum(moneys[i : i + m])) #이부분때문에 시간초과 < 이동할떄 이전꺼 뺴고, 새로운거 넣는식으로 하자!
    pre_moneys = pre_moneys - moneys[i - 1] + moneys[i + m - 1]
    max_moneys = max(max_moneys, pre_moneys) #이부분때문에 시간초과 < 이동할떄 이전꺼 뺴고, 새로운거 넣는식으로 하자!
    

print(max_moneys)