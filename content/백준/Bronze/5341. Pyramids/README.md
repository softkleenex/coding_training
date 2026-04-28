---
title: "[Bronze V] Pyramids - 5341"
tags: ["백준", "Bronze V"]
---

# [Bronze V] Pyramids - 5341 

[문제 링크](https://www.acmicpc.net/problem/5341) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2024년 11월 7일 14:46:03

### 문제 설명

<p>A pyramid of blocks is constructed by first building a base layer of n blocks and then adding n-1 blocks to the next layer. This process is repeated until the top layer only has one block.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 292px; height: 161px;"></p>

<p>You must calculate the number of blocks needed to construct a pyramid given the size of the base. For example, a pyramid that has a base of size 4 will need a total of 10 blocks.</p>

### 입력 

 <p>The input will be a sequence of integers, one per line. The end of input will be signaled by the integer 0, and does not represent the base of a pyramid. All integers, other than the last (zero), are positive.</p>

### 출력 

 <p>For each positive integer print the total number of blocks needed to build the pyramid with the specified base.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include<stdio.h>

#include<string.h>

#include<stdlib.h>

void total(int base)

{

	int ans = 0;	for(int a = base; a > 0; a--)

	{

		ans += a;

		}	

	printf("%d", ans);

	}

int main(int argc, char *argv[])

{

	int in = 0;

	int try = 0;

	while(1)

	{

		scanf("%d", &in);

		try++;

		if (in == 0) break;

		

		if(try > 1)

			printf("\n");

		

		total(in);

		}

	

		

	return 0;	

}
```
