---
title: "[AtCoder] B_Sensor_Data_Logging"
tags: ["AtCoder", "abc453"]
---

# B_Sensor_Data_Logging

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc453** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc453/tasks/abc453_b)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
특정 측정에서, 센서는 0, 1, ..., T시간에 측정됩니다. 또한 다음 규칙을 따릅니다.
0 time에서, 읽기 내용이 저장됩니다.
0, 2,...,T 시간에서, 측정값은 현재와 가장 최근의 측정값이 적어도 X일떄 저장됩니다.
센서가 읽는 값은 시간에 의해서 결정되고 time i = 0, 1,..., T라면, A_i입니다.
측정값이 저장된 시간과 저장된 값을 시간순서대로 출력하라.




## 💻 코드

```python
t, x = map(int, input().split())
a = list(map(int, input().split()))
pev = a[0]
print(0, a[0])
for i in range(len(a)):
    if abs(a[i] - pev) >= x:
        print(i, a[i])
        pev = a[i]

```
