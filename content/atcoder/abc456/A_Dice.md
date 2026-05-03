---
title: "[AtCoder] A_Dice"
tags: ["AtCoder", "abc456"]
---

# A_Dice

이 문제는 AtCoder에서 푼 문제입니다. 
이 문제는 **abc456** 콘테스트 문제입니다. 

🔗 [문제 바로가기](https://atcoder.jp/contests/abc456/tasks/abc456_a)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
6개의 면이 있는 세개의 귀사위가 있다(1~6까지의 값이 적혀져있는)
3개의 주사위가 동시에 굴러질때, 값의 총합이 X가 될 수 있는가?

X가 3부터  6 * 3 = 18 이하라면, Yes이고, 아니라면 No

## 💻 코드

```python
X = int(input())
ans = "Yes" if 3 <= X <= 18 else "No"
print(ans)
```
