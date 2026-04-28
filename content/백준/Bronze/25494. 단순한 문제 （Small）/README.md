---
title: "[Bronze IV] 단순한 문제 (Small) - 25494"
tags: ["백준", "Bronze IV"]
---

# [Bronze IV] 단순한 문제 (Small) - 25494 

[문제 링크](https://www.acmicpc.net/problem/25494) 

### 성능 요약

메모리: 1116 KB, 시간: 88 ms

### 분류

수학, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2024년 11월 8일 11:44:24

### 문제 설명

<p>세 양의 정수 $a$, $b$, $c$가 주어질 때, 다음 조건을 만족하는 정수 쌍 $(x, y, z)$의 개수를 구하시오.</p>

<ul>
	<li>$1 \le x \le a$</li>
	<li>$1 \le y \le b$</li>
	<li>$1 \le z \le c$</li>
	<li>$(x\,\bmod\,y) = (y\,\bmod\,z) = (z\,\bmod\,x)$</li>
</ul>

<p>$(A\,\bmod\,B)$는 $A$를 $B$로 나눈 나머지를 의미한다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 수 $T$가 주어진다. $(1 \le T \le 100)$</p>

<p>다음 $T$개의 각 줄에는 세 정수 $a$, $b$, $c$가 공백으로 구분되어 주어진다. $(1 \le a, b, c \le 60)$</p>

### 출력 

 <p>한 줄에 하나씩 정답을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include<stdio.h>

void ans(int a, int b, int c)

{

	int count = 0;	for(int i1 = 1; i1 <= a; i1++)

	{

		for(int i2 = 1; i2 <= b; i2++)

		{

			for(int i3 = 1; i3 <= c; i3++)

			{

				if(i1 % i2 == i2 % i3 && i2 % i3 == i3 % i1)

				{

					count++;

					}

				}	

			}		

		}

	printf("%d", count);

	

	}

int main(int argc, char *argv[])

{

int t = 0; scanf("%d",  &t);

for(int i = 0; i < t; i++)

{

	int a, b, c= 0; scanf("%d %d %d", &a, &b, &c);

	ans(a, b, c);

	if(i < t-1)	printf("\n");

}

		

	return 0;			

}
```
