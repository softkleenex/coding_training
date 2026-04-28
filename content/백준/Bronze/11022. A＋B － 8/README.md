---
title: "[Bronze V] A+B - 8 - 11022"
tags: ["백준", "Bronze V"]
---

# [Bronze V] A+B - 8 - 11022 

[문제 링크](https://www.acmicpc.net/problem/11022) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력 

 <p>각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include<stdio.h>



int main(int argc, char *argv[])
{
	int T = 0;
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
	{
		int a = 0; int b = 0;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d", i,  a, b, a+b);
		if(i != T) printf("\n");
		}
	
	
	
	
	return 0;
}
```
