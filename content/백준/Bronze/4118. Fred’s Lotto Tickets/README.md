---
title: "[Bronze III] Fred’s Lotto Tickets - 4118"
tags: ["백준", "Bronze III"]
---

# [Bronze III] Fred’s Lotto Tickets - 4118 

[문제 링크](https://www.acmicpc.net/problem/4118) 

### 성능 요약

메모리: 32412 KB, 시간: 172 ms

### 분류

구현

### 제출 일자

2025년 2월 25일 23:11:10

### 문제 설명

<p>Fred likes to play the lotto. Whenever he does, he buys lots of tickets. Each ticket has 6 unique numbers in the range from 1 to 49, inclusive. Fred likes to “Cover all his bases.” By that, he means that he likes for each set of lottery tickets to contain every number from 1 to 49, at least once, on some ticket. Write a program to help Fred see if his tickets “Cover all the bases.” </p>

### 입력 

 <p>The input file consists of a number of test cases. Each case starts with an integer N (1 <= N <= 100), indicating the number of tickets Fred has purchased. On the next N lines are the tickets, one per line. Each ticket will have exactly 6 integers, and all of them will be in the range from 1 to 49 inclusive. No ticket will have duplicate numbers, but the numbers on a ticket may appear in any order. The input ends with a line containing only a 0. </p>

### 출력 

 <p>Print a list of responses for the input sets, one per line. Print the word Yes if every number from 1 to 49 inclusive appears in some lottery ticket in the set, and No otherwise. Print these words exactly as they are shown. Do not print any blank lines between outputs. </p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 프레드는 로또를 좋아합니다. 그는 로또를 할 때마다 많은 티켓을 삽니다. 각 티켓에는 1에서 49까지의 범위에 있는 6개의 고유한 숫자가 있습니다. 프레드는 "모든 베이스를 커버하는" 것을 좋아합니다. 즉, 그는 각 복권 세트에 1에서 49까지의 모든 숫자가 적어도 한 번씩은 어떤 티켓에 포함되기를 좋아한다는 뜻입니다. 프레드가 자신의 티켓이 "모든 베이스를 커버하는지" 확인할 수 있도록 돕는 프로그램을 작성하세요. 

# 입력
# 입력 파일은 여러 테스트 케이스로 구성되어 있습니다. 각 케이스는 정수 N(1 <= N <= 100)으로 시작하며, 이는 Fred가 구매한 티켓 수를 나타냅니다. 다음 N줄에는 티켓이 한 줄에 하나씩 있습니다. 각 티켓은 정확히 6개의 정수를 가지며, 모두 1에서 49까지의 범위에 속합니다. 티켓에는 중복된 숫자가 없지만 티켓의 숫자는 어떤 순서로든 나타날 수 있습니다. 입력은 0만 포함된 줄로 끝납니다. 

# 출력
# 입력 세트에 대한 응답 목록을 줄당 하나씩 인쇄합니다. 세트의 복권에 1에서 49까지의 모든 숫자가 나타나면 Yes를 인쇄하고, 그렇지 않으면 No를 인쇄합니다. 이 단어들을 표시된 대로 정확히 인쇄합니다. 출력 사이에 빈 줄을 인쇄하지 마십시오. 
#print([x for x in range(1, 50)])

nums = []

while 1:
    n = int(input().strip())
    temp = []
    if n == 0:
        break  
    for i in range(0, n):
        temp+= ((map(int, input().split())))
    nums.append(temp)

#print(nums)
    
for i in nums:
    temp = list(set(i))
    temp.sort()
    if (temp == [int(x) for x in range(1, 50)]):
        print("Yes", end = '')
    else:
       print("No", end = '')

    if i != nums[len(nums) - 1]:
        print()
```
