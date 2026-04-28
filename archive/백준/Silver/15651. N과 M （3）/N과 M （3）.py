# https://www.acmicpc.net/problem/15651

n,m = map(int, input().split())
#~n 까지, m개 고르기

n = list(i for i in range(1, n + 1))

ans = []

def back(buck):#now는 n의 인덱스, buck은 현재 바구니
    if len(buck) == m:#바구니의 길이가 m개라면, 즉 고를수 있는만큼 골랐다면
        ans.append(buck)#현재 바구니를 정답지에 추가한다
        return
    
    
    for i in range(0, len(n)):
        back(buck + [n[i]])



back([])

# print(ans)

ans.sort()

for v in ans:
    print(*v, sep = ' ')