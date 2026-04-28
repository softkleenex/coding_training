---
title: "[Bronze III] 삼각형 분류 - 9366"
tags: ["백준", "Bronze III"]
---

# [Bronze III] 삼각형 분류 - 9366 

[문제 링크](https://www.acmicpc.net/problem/9366) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

수학, 구현, 기하학, 사칙연산, 많은 조건 분기

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>꿍은 오늘 학교에서 삼각형에 대해 배웠다. 삼각형은 변의 길이에 따라 다음과 같이 분류될 수 있다.</p>

<ul>
	<li>정삼각형(equilateral triangle)은 모든 변의 길이가 같다. 각 역시 60도로 모두 같다.</li>
	<li>이등변삼각형(isosceles triangle)은 두 개의 변의 길이가 같다. 각 역시 두 개의 각의 크기가 같다.</li>
	<li>부등변삼각형(scalene triangle)은 모든 변의 길이가 같지 않다. 각 역시 모두 다르다. 몇몇 부등변삼각형의 경우 직각삼각형이다.</li>
</ul>

<p>수학선생님이 삼각형의 세 변의 길이를 가지고 삼각형을 분류하라는 숙제를 내줬는데 꿍은 정말 놀고싶다. 꿍이 놀수있도록 여러분이 도와주어라.</p>

### 입력 

 <p>입력의 첫 줄에는 테스트케이스의 개수 T(1 <= T <= 100)가 주어진다. 다음 T줄에는 각 줄에 삼각형의 세 변을 나타내는 3개의 정수 A,B,C(1 <= A,B,C <= 1,000,000)가 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해 삼각형이 “equilateral”, “isosceles”, “scalene” 타입 중 어느 타입에 속하는지 출력한다. 만약 주어진 세 변의 길이로 삼각형이 만들어지지 않을경우, “invalid!”를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include<stdio.h>

#include<stdlib.h>

#include<string.h>

int check(int a, int b, int c)

{

	int i = a > b ? a : b;	i = i > c ? i : c;

	int other = a + b + c - i;

	

	if(other <= i)

	{

			printf("invalid!");

			return 0;

	}

	return 1;

}

void ans()

{

	int a, b, c = 0; scanf("%d %d %d", &a, &b, &c);

	

	if(0 == check(a, b, c)) return ;

	

	else if(a == b && b == c && c == a)//all same

	{

		printf("equilateral");

		}

	else if(a == b || b == c || c == a)//only two same

	{

		printf("isosceles");

		}		

	else//noting same

	{

		printf("scalene");

		}	

	}

int main(int argc, char *argv[])

{

	int t = 0; scanf("%d", &t);

	for(int i = 0; i < t; i++)

	{

		printf("Case #%d: ", i+1);

		ans();

		if (i < t -1) printf("\n");

		}

	

		

			return 0;	

}
```
