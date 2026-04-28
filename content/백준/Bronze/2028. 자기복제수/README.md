---
title: "[Bronze II] 자기복제수 - 2028"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 자기복제수 - 2028 

[문제 링크](https://www.acmicpc.net/problem/2028) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

수학

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>어떤 자연수 N을 제곱했을 때, 그 제곱수의 맨 뒷자리에 원래의 수 N이 다시 나타나면, 우리는 그 수 N을 자기복제수라고 한다.</p>

<p>예를 들면, 5의 제곱은 5<sup>2</sup>는 25이고 25의 맨 뒷자리에 원래의 수 5가 나타나므로 5는 자기복제수이다. 또 다른 예로, 76의 제곱은 5776이고 5776의 맨 뒷자리에 76이 나타나므로 76 또한 자기복제수이다.</p>

<p>자연수 N이 주어졌을 때, 그 수가 자기복제수인지 아닌지를 알아내는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력의 첫 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 자연수 N (1 ≤ N ≤ 1000)이 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해, 주어진 자연수가 자기복제수이면 YES를 아니면 NO를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include<stdlib.h>

#include<stdio.h>

#include<string.h>

int arr[20];

int n;

int degree(int data)

{

	int degree = 0;	if(data / 1000 >= 1)

	{

		degree = 10000;

		}

	else if(data / 100 >= 1)

	{

		degree = 1000;

		}

	else if(data / 10 >= 1)

	{

		degree = 100;

		}

	else if(data / 1 >= 1)

	{

		degree = 10;

		}

	return degree;

}

void check(int data)

{

	int a = (data*data) % degree(data);

	if(a == data)

		printf("YES\n");

	else

		printf("NO\n");

		

}	

	

	

int main(int argc, char *argv[])

{

	 scanf("%d", &n);

	

	for(int a = 0; a < n; a++)

	{

		scanf("%d", &arr[a]);

	}

	

		

	for(int a = 0; a < n; a++)

	{

		check(arr[a]);

	}	

	

		return 0;						

}
```
