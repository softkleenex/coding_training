---
title: "[AtCoder] C_Vanish"
tags: ["AtCoder", "abc455"]
---

# C_Vanish

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc455** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc455/tasks/abc455_c)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

정수 sequence A가 주어진다. (A = (A_1, A_2,..., A_N))
수열 A의 총합의 최솟값을 찾아라 다음 작업을 K번 반복한 다음에.
- 정수 x를 선택한다. 각각의 A_i = x인 i에 대해서, A_i의 값을 0 으로 변경한다.


A에 대해서 collections.Counter을 수행한 다음, Counter의 key 와 value를 곱한 리스트를 만든다.(이 리스트의 총 합이 A의 sum과 같음에 유의)
그 이후, A를 정렬한다음에 0 ~ len(A) - k의 sum을 출력한다. 이때 k가 len(A)보다 같거나 큰 경우에 대해 예외처리가 필요하다.


## 💻 코드

```python
import collections
from collections import Counter

n, k = map(int, input().split())
a = Counter(list(map(int, input().split()))).items()

a = sorted(list(x[0] * x[1] for x in a))
# print(a)

a = sum(a[0 : len(a) - k]) if len(a) - k > 0 else 0

print(a)


```
