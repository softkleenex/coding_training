---
title: "[AtCoder] B_Spiral_Galaxy"
tags: ["AtCoder", "abc455"]
---

# B_Spiral_Galaxy

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc455** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc455/tasks/abc455_b)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
H row와 w col을 가진 grid가 있다. 위에서부터 u 번쨰 cell 과 왼쪽에서부터 j번쨰 col 은 (i, j) 라고 표현한다.
grid의 각 cell은 흰색, 혹은 검정색으로 색칠되어진다. 그리드의 정보는 길이 W인 H string, S_1,S_2,S_3... , 로 주어진다.: cell (i, j)는 S_i의 j번째 문자가 . 이라면 white, #라면 black이다.

점대칭적으로 색칠되어있는 지역의 수를 찾아라.
좀더 포멀하게, 정수 튜플(h_1, h_2, w_1, w_2)의 수를 찾아라. 다음의 조건을 만족하는

1 <= h_1 <= h_2 <= H

1<= w_1 <= w_2 <= W

h_1<= i <= h_2
w_1 <= j <= w_2인 i, j 에 대해서,

(i, j) cell과 (h_1 + h_2 - i, w_1 + w_2 - j) 는 같은 색을 가지고 있다.


## 💻 코드

```python
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


```
