---
title: "[AtCoder] C_Sneaking_Glances"
tags: ["AtCoder", "abc453"]
---

# C_Sneaking_Glances

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc453** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc453/tasks/abc453_c)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
이 문제의 입력값 $N$은 최대 20으로, 모든 경우를 고려할 때 경로의 가짓수는 $2^{20}$가지입니다. 각 경로를 탐색하는 데 $O(N)$의 시간이 소요되므로, 전체 시간 복잡도는 $O(N \cdot 2^N)$이 됩니다.이는 약 2,000만 번의 연산으로 이론적으로는 제한 시간 내에 계산 가능한 범위에 있습니다. 하지만 파이썬의 반복문 오버헤드로 인해 CPython(Python 3) 환경에서는 지속적으로 TLE가 발생하였습니다. 이를 해결하기 위해 다음과 같은 최적화를 수행했습니다:좌표 정수화: 실수 오차를 방지하고 연산 효율을 높이기 위해 모든 좌표에 2를 곱하여 정수 연산으로 처리했습니다.지역 변수 최적화: 전역 공간보다 실행 속도가 빠른 solve() 함수 내에 로직을 구현하여 변수 접근 속도를 높였습니다.실행 환경 변경: 제출 언어를 PyPy 3로 변경하여 JIT 컴파일러를 통한 실행 속도 최적화를 적용했습니다.

The input $N$ is at most 20, meaning there are $2^{20}$ possible paths. Since each path takes $O(N)$ to evaluate, the total time complexity is $O(N \cdot 2^N)$.While this is theoretically within the limits (approx. $2 \times 10^7$ operations), the standard CPython interpreter caused TLE due to loop overhead. To resolve this, I implemented the following optimizations:Integer Arithmetic: Multiplied all coordinates by 2 to avoid floating-point issues and improve performance.Local Scope Optimization: Wrapped the logic inside a solve() function to leverage faster local variable access.Language Selection: Switched to PyPy 3 to utilize its JIT compiler, significantly reducing execution time.

## 💻 코드

```python
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L = [int(x) * 2 for x in L]

    max_ans = 0


    #2^N 가지의 모든 경우의 수를 비트로 표현한다(00000...0 ~ 111...1)
    for i in range(1 << N):
        curr = 1
        count = 0

        for j in range(N):
            if(i >> j) & 1: #j번쨰 경로를 꺼내서, 1인지 체크한다.
                next_pos = curr + (L[j])
            else:
                next_pos = curr - (L[j])
            if curr * next_pos < 0:
                count += 1

            curr = next_pos
        if count > max_ans:
            max_ans = count

    print(max_ans)


solve()

```
