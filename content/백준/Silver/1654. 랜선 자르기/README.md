---
title: "[Silver II] 랜선 자르기 - 1654"
tags: ["백준", "Silver II"]
---

# [Silver II] 랜선 자르기 - 1654 

[문제 링크](https://www.acmicpc.net/problem/1654) 

### 성능 요약

메모리: 1112 KB, 시간: 4 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2024년 10월 15일 18:02:08

### 문제 설명

<p>집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.</p>

<p>이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)</p>

<p>편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 2<sup>31</sup>-1보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#include <math.h>

#include <limits.h>

long long K;

long long *arr1;

long long N;

long long ans(long long left, long long right, long long postlen)

{

	long long mid = (left + right) / 2;	long long now_lencount = 0;

	long long next_len = postlen;

		for (long long a = 0; a < K; a++)

		{

			now_lencount += arr1[a] / mid;

			//현재 값으로 arr[a]를 통해 만들어지는 랜선의 개수 구하기!

		}

	

	

	if (now_lencount >= N) //갯수 충족시에

	{

		if(postlen > mid)//전의 길이보다 적으면?

			{

				left = mid+1;//더 길게 try

				next_len = postlen;				

			}

		else if(postlen < mid)//전의 길이보다 크면?

			{

				left = mid+1;//더 길게 try

				next_len = mid;

			}

	}

	else if (now_lencount < N) //갯수 미충족

	{//짧게 try

		right = mid-1;

		next_len = postlen;

	}

	//현 단게 ans기반 left right 조정 끝

	

	//재귀 여부를 결정하자!

	if (left > right)//종료

	{

		printf("%lld", next_len);//가장 최적의 lens출력

		return mid;

	}

	else

	{

		return (ans(left, right, next_len));

	}

	return 0;

}

int main(int argc, char *argv[])

{

	scanf("%lld", &K); //보유 랜선 개수

	scanf("%lld", &N); //필요 랜선 개수

	arr1 = (long long *)malloc(sizeof(long long) * K);

	long long min_len = 1; //최소 길이

	long long max_len = 0; //최대 길이(K개의 랜선중에 가장 큰길이

	for (long long a = 0; a < K; a++)

	{

		scanf("%lld", &arr1[a]);

	}

	for (long long i = 0; i < K; i++)

	{

		max_len = (max_len > arr1[i]) ? (max_len) : (arr1[i]);

	}

	ans(min_len, max_len, 0); //1 ~ max로 이분탐색 시행 - N와 랜선 길이 범위가 매우 크다!

	

	free(arr1);

	return 0;

}
```
