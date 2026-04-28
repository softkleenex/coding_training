---
title: "[Bronze I] 희주의 수학시험 - 8974"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 희주의 수학시험 - 8974 

[문제 링크](https://www.acmicpc.net/problem/8974) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>강민이 동생 희주는 올해 초등학교에 입학했다. 며칠 있으면, 생애 첫 시험을 보게 될텐데, 수학시험도 같이 본다고 한다.</p>

<p>희주는 겁을 먹은 나머지, 열심히 준비해야겠다고 생각했다. 이를 본 오빠 강민이는 동생 희주를 위해 작은 도움을 주고자 한다.</p>

<p>연습문제 중에 하나가 정수를 적어나가는 것이였는데 수열은 1이 한 개, 2가 두 개, 3이 세 개.. 와 같이 만들어진다.</p>

<p>이제 강민이는 희주에게 두 개의 정수 A, B를 부를텐데, 그럼 희주는 주어진 수열에서 A번째와 B번째 사이에 있는 모든 수들의 합을 말해야한다.</p>

<p>예를 들면, A가 1이고 B는 3이라면 답은 처음 세 개의 정수를 더한 1+2+2 = 5 가 된다.</p>

<p>희주에게 문제를 내기 위해 정답을 계산하는 프로그램을 작성하시오.</p>

### 입력 

 <p>한 줄에 양의 정수 A와 B가 주어진다. (1 ≤ A ≤ B ≤ 1000)</p>

### 출력 

 <p>희주가 대답해야 할 정답을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
//https://www.acmicpc.net/problem/8974

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

int sum(int a)

{ //intput a, >return 1+2... +a;

	int sum = 0;	for (int i = 0; i <= a; i++)

	{

		sum += i;

	}

	return sum;

}

int main()

{

	int A, B;

	scanf("%d %d", &A, &B);

	int *arr = (int *)malloc(sizeof(int) * (B + 100)); //0 ~ B

	//0 1 2 2 3 3 3 4 4 4 4 5 5 5 5...

	int k = 0;

	for (int index = 0; index <= B + 1; index++)

	{

		arr[index] = k;

		if (index == sum(k)) //

		{

			k++;

		}

	}

	//0 > 0, 1 > 1, 1+1 > 2, 1+2 > 2, 1+2 + 1 > 3,,,,, 1+2+3 > 3, ,,,, 0+1+2+3+4 > 4,,,,

	for (int a = 0; a <= B; a++)

	{

		//		printf("%d  ", arr[a]);

		//		if(a == B) printf("\n");

	}

	int ans = 0;

	for (int a = A; a <= B; a++)

	{

		ans += arr[a];

	}

	printf("%d", ans);

	return 0;

}
```
