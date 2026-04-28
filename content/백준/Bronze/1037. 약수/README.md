---
title: "[Bronze I] 약수 - 1037"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 약수 - 1037 

[문제 링크](https://www.acmicpc.net/problem/1037) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

수학, 정수론

### 제출 일자

2024년 10월 20일 13:09:33

### 문제 설명

<p>양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.</p>

### 출력 

 <p>첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int max(int arr1[],int len)
{
	int max = arr1[0];
	for(int a = 0; a < len; a++)
	{
		max = max >= arr1[a] ? max : arr1[a];
		}
	
	return max;
	}
int min(int arr1[],int len)
{
	int min = arr1[0];
	for(int a = 0; a < len; a++)
	{
		min = min <= arr1[a] ? min : arr1[a];
		}
	
	return min;
}
	
int main(int argc, char *argv[])
{
	int count = 0; scanf("%d", &count);
	int* arr1; arr1 = (int*)malloc(sizeof(int) * count);
	for(int a = 0; a < count; a++)
	{
		scanf("%d", &arr1[a]);
	}
	if(count == 1)
		printf("%d", arr1[0] * arr1[0]);
	else
		{
			printf("%d", min(arr1, count) * max(arr1, count));
			}	
	
	return 0;
}
```
