---
title: "[AtCoder] B_Mapping"
tags: ["AtCoder", "abc454"]
---

# B_Mapping

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc454** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc454/tasks/abc454_b)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
1 부터 N까지의 숫자가 할당된 사람이있다
1 부터 M까지의 숫자가 할당된, M가지 타입의 옷이 있다. 사람 i는 F_i의 옷을 입는다.
다음의 질문에 대해서 Yes or No로 대답하라.
1. 모든 N 명의 사람이 다른 타입의 옷을 입고있는가?
2. M종류의 옷들 하나하나에 대하여, 그 옷을 입고ㄴ있는 최소 하나의 사람이 존재하는가?

1번은 list와 set의 길이로, 2번은 flag를 통하여 해결하였다.


## 💻 코드

```python
N, M = map(int, input().split())
F = list(map(int, input().split()))

print("Yes") if len(F) == len(set(F)) else print("No")

flag = 0
for v in range(1, M + 1):
    if not(v in F):
        flag = 1

print("Yes") if flag == 0 else print("No")

```
