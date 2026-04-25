# https://www.acmicpc.net/problem/2992

# 문제
# 정수 X가 주어졌을 때, X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력한다.

# 수의 구성이 같다는 말은, 수를 이루고 있는 각 자리수가 같다는 뜻이다. 예를 들어, 123과 321은 수의 구성이 같다. 하지만, 123과 432는 구성이 같지 않다.

# 입력
# 첫째 줄에 X가 주어진다. (1 ≤ X ≤ 999999) X는 0으로 시작하지 않는다.

# 출력
# 첫째 줄에 결과를 출력한다. 만약 그러한 숫자가 없는 경우에는 0을 출력한다.

# 예제 입력 1 
# 156
# 예제 출력 1 
# 165
# 예제 입력 2 
# 330
# 예제 출력 2 
# 0
# 예제 입력 3 
# 27711
# 예제 출력 3 
# 71127
# 출처
# Contest > Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #4 2번

# 문제를 번역한 사람: baekjoon

s = input()

x = list(s)
n = len(x)

x2 = int(s)

visited = [-1 for i in range(n)]


# print(x)
# print(x2)


now = 0

buck = []
ans = []

def back(buck):
    if len(buck) == len(x):
        if int("".join(buck)) > x2:
            ans.append("".join(buck))
        return
    
    for i in range(n):
        if visited[i] == -1:
            visited[i] = 1
            back(buck + [x[i]])
            visited[i] = -1
                

back([])


if len(ans) == 0:
    print(0)
else:
    print(min(ans))
    
    
    


#x를 하나하나의 문자로 분해하고, 백트래킹을 하면 되지않을까?