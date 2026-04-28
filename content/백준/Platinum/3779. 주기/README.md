---
title: "[Platinum IV] 주기 - 3779"
tags: ["백준", "Platinum IV"]
---

# [Platinum IV] 주기 - 3779 

[문제 링크](https://www.acmicpc.net/problem/3779) 

### 성능 요약

메모리: 128712 KB, 시간: 236 ms

### 분류

문자열, KMP

### 제출 일자

2025년 9월 28일 15:06:58

### 문제 설명

<p>아스키 코드가 97이상 126이하인 N개의 문자로 이루어진 문자열 S가 주어진다. 문자열 S의 모든 접두사에 대해, 각각의 접두사가 주기적인 문자열인지 아닌지 알고 싶다. 다시 말해 2 ≤ i ≤ N을 만족하는 각각의 i에 대해, 길이가 i인 문자열 S의 접두사가 어떤 문자열 A에 대해 A<sup>K </sup>형태로 표현할 수 있는 가장 큰 K > 1을 알아내려 한다.</p>

<p>A<sup>K</sup>란 문자열 A가 K번 연속되어있는 문자열을 의미한다. A = "<code>abad</code>"이고, K = 3인 경우 A<sup>K</sup> = "<code>abadabadabad</code>"이다.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어진다. 각 테스트 케이스는 두 줄로 이루어진다. 테스트 케이스의 첫 번째 줄에는 문자열 S의 길이인 정수 N이 주어진다 (2 ≤ N ≤ 1 000 000). 테스트 케이스의 두 번째 줄에는 문자열 S가 주어진다. 입력의 끝은 0으로 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해, "Test case #"과 테스트 케이스의 번호를 한 줄에 출력한다. 그 후, 길이가 i인 접두사의 주기가 K > 1인 경우, 접두사의 길이 i와 주기 K를 공백으로 분리하여 한 줄에 출력한다. 이때, 접두사의 길이가 오름차순이 되도록 출력하여야 한다. 각 테스트 케이스에 대한 답을 출력한 후, 빈 줄을 한 줄 출력하여야 한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
import sys
input = sys.stdin.readline
def kmp(all_string, pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            
    # #kmp
    # result = []
    # i = 0
    # for j in range(len(all_string)):
    #     while i > 0 and pattern[i] != all_string[j]:
    #         i = table[i - 1]
    #     if pattern[i] == all_string[j]:
    #         i += 1
    #         if i == len(pattern):
    #             result.append(j - i + 1)
    #             i = table[i - 1]
                
    return table




c = 1

while(1):

    t = int(input().strip())
    if t == 0:
        break
    
    
    s = input().strip()
    print(f"Test case #{c}")
    c += 1
    ans = kmp(s, s)
    # print(ans)
    
    for i, v in enumerate(ans):
        if ans[i] > 0:  # failure 값이 0보다 클 때만 
            period_len = (i + 1) - ans[i]  # 현재 인덱스의 failure 값 사용
            if (i + 1) % period_len == 0:  # 완전한 주기인지 확인
                period_freq = (i + 1) // period_len
                print(period_len * period_freq, period_freq)
    print()
```
