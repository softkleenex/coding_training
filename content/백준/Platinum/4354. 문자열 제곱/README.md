---
title: "[Platinum V] 문자열 제곱 - 4354"
tags: ["백준", "Platinum V"]
---

# [Platinum V] 문자열 제곱 - 4354 

[문제 링크](https://www.acmicpc.net/problem/4354) 

### 성능 요약

메모리: 205604 KB, 시간: 524 ms

### 분류

문자열, KMP

### 제출 일자

2025년 9월 25일 14:50:42

### 문제 설명

<p>알파벳 소문자로 이루어진 두 문자열 a와 b가 주어졌을 때, a*b는 두 문자열을 이어붙이는 것을 뜻한다. 예를 들어, a="abc", b="def"일 때, a*b="abcdef"이다.</p>

<p>이러한 이어 붙이는 것을 곱셈으로 생각한다면, 음이 아닌 정수의 제곱도 정의할 수 있다.</p>

<ul>
	<li>a^0 = "" (빈 문자열)</li>
	<li>a^(n+1) = a*(a^n)</li>
</ul>

<p>문자열 s가 주어졌을 때, 어떤 문자열 a에 대해서 s=a^n을 만족하는 가장 큰 n을 찾는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 10개 이하의 테스트 케이스로 이루어져 있다. 각각의 테스트 케이스는 s를 포함한 한 줄로 이루어져 있다. s의 길이는 적어도 1이며, 백만글자를 넘지 않는다. 마지막 테스트 케이스의 다음 줄은 마침표이다.</p>

### 출력 

 <p>각각의 테스트 케이스에 대해, s=a^n을 만족하는 가장 큰 n을 찾은 뒤 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/4354
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
        
    result = []
    i = 0
    
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i -1]
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i - 1]
                
    return table

while(1):
    s = input().strip()
    len_s = len(s)
    ans = 1
    if s == '.':
        break
    else:
        ans = kmp(s, s)
        # print(ans)
        if len(s) % (len(s) - ans[-1]) == 0:
            print(len(s) // (len(s) - ans[-1]))
        else:
            print(1)
```
