---
title: "[Bronze II] Grid Pattern - 14539"
tags: ["백준", "Bronze II"]
---

# [Bronze II] Grid Pattern - 14539 

[문제 링크](https://www.acmicpc.net/problem/14539) 

### 성능 요약

메모리: 111516 KB, 시간: 128 ms

### 분류

구현, 문자열

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>Games that are commonly found in the Unix System during the 70s and 80s are design in text mode. Grid is the basic layout for many of these games where pieces or items are positioned in rows and columns. Classic examples would be tic-tac-toe, chess and minesweeper. You are to design a simple text-based grid layout engine that can be used in the games.</p>

<p>Given specified dimensions, print a text-based grid pattern. Use the | (pipe) sign to print vertical elements, the – (minus) to print horizontal ones and + (plus) for crossing. The rest of the spaces are filled with * (asterisk).</p>

### 입력 

 <p>The first line of input contains a positive integer <em>N</em> (<em>N</em> ≤ 100) which indicates the number of test cases. Each of the following <em>N</em> lines contains four positive integers: <em>row</em> – the number of rows, <em>col</em> – the number of columns, <em>w</em> and <em>h</em> – the width and height of the single grid respectively. (1 ≤ <em>row</em>, <em>col</em> ≤ 10; 1 ≤  <em>w</em>, <em>h</em> ≤ 5 )</p>

### 출력 

 <p>For each test case, output a line in the format "Case #x:" where x is the case number (starting from 1), follow by the grid pattern as shown in the sample output.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 문제
# Games that are commonly found in the Unix System during the 70s and 80s are design in text mode. Grid is the basic layout for many of these games where pieces or items are positioned in rows and columns. Classic examples would be tic-tac-toe, chess and minesweeper. You are to design a simple text-based grid layout engine that can be used in the games.

# Given specified dimensions, print a text-based grid pattern. Use the | (pipe) sign to print vertical elements, the – (minus) to print horizontal ones and + (plus) for crossing. The rest of the spaces are filled with * (asterisk).

# 입력
# The first line of input contains a positive integer N (N ≤ 100) which indicates the number of test cases. Each of the following N lines contains four positive integers: row – the number of rows, col – the number of columns, w and h – the width and height of the single grid respectively. (1 ≤ row, col ≤ 10; 1 ≤  w, h ≤ 5 )

# 출력
# For each test case, output a line in the format "Case #x:" where x is the case number (starting from 1), follow by the grid pattern as shown in the sample output.

import sys

input = sys.stdin.readline


n = int(input())

for _ in range(0, n):
    case = _ + 1
    print(f'Case #{case}:')
    #row, col, w, h = map(int, input().split())#차예대로 행, 열, 단일 그리드의 너비(가로), 높이(세로)
    h, w, col, row = map(int, input().split())#차예대로 행, 열, 단일 그리드의 너비(가로), 높이(세로)



    floor = (['+'] +  (['-'] * col)) * w  + ['+']
    
    grid1 = [['*'] * col] * row
    

    print(*floor, sep ='')
    for i in range(0, h):
        for i2 in grid1:
            for i3 in range(w):
                print('|', end = '')
                print(*i2, sep = '', end = '')
            print('|')
        print(*floor, sep = '')
        

   
```
