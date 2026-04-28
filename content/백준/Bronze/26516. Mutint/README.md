---
title: "[Bronze II] Mutint - 26516"
tags: ["백준", "Bronze II"]
---

# [Bronze II] Mutint - 26516 

[문제 링크](https://www.acmicpc.net/problem/26516) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 5일 16:37:51

### 문제 설명

<p>A “Mutint” is an integer M that is changed according to certain criteria, such as in this problem. Given a positive integer, change M according to the following rules.</p>

<ol>
	<li>Find the leftmost largest digit D of M.</li>
	<li>If D is odd, change it to a zero.</li>
	<li>If D is even, add 4 to that digit. If the sum exceeds 9, change D to the one’s place of the sum.</li>
</ol>

### 입력 

 <p>Several integers, each on one line. The end of input is signaled with a zero on the last line. All integers, except the last integer, are positive.</p>

### 출력 

 <p>M, according to the rules above. M cannot have leading zeros.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# A “Mutint” is an integer M that is changed according to certain criteria, such as in this problem. Given a positive integer, change M according to the following rules.

# Find the leftmost largest digit D of M.
# If D is odd, change it to a zero.
# If D is even, add 4 to that digit. If the sum exceeds 9, change D to the one’s place of the sum.
# 입력
# Several integers, each on one line. The end of input is signaled with a zero on the last line. All integers, except the last integer, are positive.

# 출력
# M, according to the rules above. M cannot have leading zeros.

a = -1

while 1:
    a = map(str, input())
    
    a = ''.join(a)
    
    a = list(map(int, a))
    
    #print(a)

    if a == [0]:
        quit()
    
    #print(a.index(max(a)))
    if max(a) % 2 == 1:
        a[a.index(max(a))] = 0
    else:
        temp = (max(a) + 4)% 10
        a[a.index(max(a))] = temp
    try:
        while(a[0] == 0):
            a.pop(0)
    except:
        pass
    
    print(*a, sep = '')
```
