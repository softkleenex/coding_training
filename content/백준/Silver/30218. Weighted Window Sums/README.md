---
title: "[Silver III] Weighted Window Sums - 30218"
tags: ["백준", "Silver III"]
---

# [Silver III] Weighted Window Sums - 30218 

[문제 링크](https://www.acmicpc.net/problem/30218) 

### 성능 요약

메모리: 152840 KB, 시간: 548 ms

### 분류

수학, 정렬, 누적 합, 슬라이딩 윈도우

### 제출 일자

2025년 4월 13일 15:07:31

### 문제 설명

<p>Given a sequence of numbers, we define a window within the sequence to be a contiguous subsequence of those numbers. For example, in the sequence [3, 6, 2, 3, 5, 4], there are four windows of size 3: [3, 6, 2], [6, 2, 3], [2, 3, 5] and [3, 5, 4]. We call window i of size k the window which starts with the i<sup>th</sup> value in the list and includes exactly k consecutive values, ending with the (i+k-1)<sup>th</sup> value in the list.</p>

<p>For a window with values a<sub>1</sub>, a<sub>2</sub>, …, a<sub>k</sub>, define its weighted window sum to be:</p>

<p style="text-align: center;">1a<sub>1</sub> + 2a<sub>2</sub> + 3a<sub>3</sub> + … + ka<sub>k</sub></p>

<p>For the four window sums described above, the corresponding weighted window sums are:</p>

<p style="text-align: center;">[3, 6, 2] → 1 × 3 + 2 × 6 + 3 × 2 = 21 (Rank 2)</p>

<p style="text-align: center;">[6, 2, 3] → 1 × 6 + 2 × 2 + 3 × 3 = 19 (Rank 1)</p>

<p style="text-align: center;">[2, 3, 5] → 1 × 2 + 2 × 3 + 3 × 5 = 23 (Rank 3)</p>

<p style="text-align: center;">[3, 5, 4] → 1 × 3 + 2 × 5 + 3 × 4 = 25 (Rank 4)</p>

<p>For each window of a given size within a sequence of numbers, we sort those windows in increasing order of weighted window sum, breaking ties by the starting index of the window, from smallest index to largest index.</p>

<p>Given a sequence of integers and the size of a window, sort each window of the given size in the sequence by weighted window sum in increasing order, breaking ties by the starting index of the window.</p>

### 입력 

 <p>The first input line contains two integers: n (1 ≤ n ≤ 2 × 10<sup>5</sup>) and k (1 ≤ k ≤ n), representing the length of the sequence and the size of the window. Each of the next n input lines will contain one number of the sequence, in order. Each of these values will be in between 1 and 10<sup>8</sup>, inclusive.</p>

### 출력 

 <p>Print a sorted list of the windows, with one window per line. For each window, output its starting index, followed by the weighted window sum of that window.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 문제
# Given a sequence of numbers, we define a window within the sequence to be a contiguous subsequence of those numbers. For example, in the sequence [3, 6, 2, 3, 5, 4], there are four windows of size 3: [3, 6, 2], [6, 2, 3], [2, 3, 5] and [3, 5, 4]. We call window i of size k the window which starts with the ith value in the list and includes exactly k consecutive values, ending with the (i+k-1)th value in the list.

# For a window with values a1, a2, …, ak, define its weighted window sum to be:

# 1a1 + 2a2 + 3a3 + … + kak

# For the four window sums described above, the corresponding weighted window sums are:

# [3, 6, 2] → 1 × 3 + 2 × 6 + 3 × 2 = 21 (Rank 2)

# [6, 2, 3] → 1 × 6 + 2 × 2 + 3 × 3 = 19 (Rank 1)

# [2, 3, 5] → 1 × 2 + 2 × 3 + 3 × 5 = 23 (Rank 3)

# [3, 5, 4] → 1 × 3 + 2 × 5 + 3 × 4 = 25 (Rank 4)

# For each window of a given size within a sequence of numbers, we sort those windows in increasing order of weighted window sum, breaking ties by the starting index of the window, from smallest index to largest index.

# Given a sequence of integers and the size of a window, sort each window of the given size in the sequence by weighted window sum in increasing order, breaking ties by the starting index of the window.

# 입력
# The first input line contains two integers: n (1 ≤ n ≤ 2 × 105) and k (1 ≤ k ≤ n), representing the length of the sequence and the size of the window. Each of the next n input lines will contain one number of the sequence, in order. Each of these values will be in between 1 and 108, inclusive.

# 출력
# Print a sorted list of the windows, with one window per line. For each window, output its starting index, followed by the weighted window sum of that window.

# 예제 입력 1 
# 6 3
# 3
# 6
# 2
# 3
# 5
# 4
# 예제 출력 1 
# 2 19
# 1 21
# 3 23
# 4 25
# 예제 입력 2 
# 7 3
# 2
# 3
# 2
# 3
# 2
# 4
# 1
# 예제 출력 2 
# 5 13
# 1 14
# 3 14
# 2 16
# 4 19

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

list1 = []
list1_sum = []

for _ in range(0, n):
    list1.append(int(input()))
    if len(list1_sum) > 0:
        list1_sum.append(list1_sum[-1] + list1[-1])
    else:
        list1_sum.append(list1[-1])



# print(list1)
# print(list1_sum)




def prefix(a, b):#a ~ b 까지의 누적합, a, b 포함
    if a - 1 < 0:
        return list1_sum[b]
    
    else:
        return list1_sum[b] - list1_sum[a - 1]


ans = [
    [ sum(    (i + 1) * list1[i] for i in range(0, k) ), 1]
       ]







for i in range(1, n - k + 1):

    now_ans = ans[-1][0] - prefix(i - 1, i + k - 2) + k * list1[i+k-1]
    ans.append([now_ans, i + 1])


ans.sort()


for i in ans:
    print(f'{i[1]} {i[0]}')
```
