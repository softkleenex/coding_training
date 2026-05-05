---
title: "[AtCoder] Not_Adjacent"
tags: ["AtCoder", "abc456"]
---

# Not_Adjacent

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc456** 콘테스트 문제입니다.

🔗 [콘테스트 문제 목록](https://atcoder.jp/contests/abc456/tasks)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
이 문제는 투 포인터로 해결가능,


## 💻 코드

```python
s = input()
n = len(s)
left = 0

ans = 0

while left  < n:
    right = left
    while right + 1 < n and s[right] != s[right + 1]:
        right += 1

    # print(s[left : right], "is valid")
    L = right - left + 1
    ans += (L)*(L + 1) // 2
    left = right + 1

print(ans % 998244353)

```
