---
title: "[Bronze I] 이항 계수 1 - 11050"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 이항 계수 1 - 11050 

[문제 링크](https://www.acmicpc.net/problem/11050) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

수학, 구현, 조합론

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))</p>

### 출력 

 <p> \(\binom{N}{K}\)를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include<stdio.h>

int ans(int num)

{

	int temp = 1;	int ans_num = 1;

	do{

		ans_num *= temp;

		temp++;

		}while(temp <= num);

		

	return ans_num;

	}

int main(int argc, char *argv[])

{

	int N = 0; int K = 0; scanf("%d %d", &N, &K);

	printf("%d", ans(N) / (ans(K) * ans(N-K)));	

	

	return 0;	

}
```
