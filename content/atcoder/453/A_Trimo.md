---
title: "[AtCoder] A_Trimo"
tags: ["AtCoder", "Unrated"]
---

# A_Trimo

이 문제는 AtCoder에서 푼 문제입니다. 문제 설명이 제공되지 않았습니다.

---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```python
n = int(input())
s = input()
flag = 0
for v in s:
    if v != 'o' or flag != 0:
        print(v, end = '')
    if v != 'o':
        flag += 1

```
