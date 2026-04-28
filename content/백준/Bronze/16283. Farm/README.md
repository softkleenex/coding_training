---
title: "[Bronze II] Farm - 16283"
tags: ["백준", "Bronze II"]
---

# [Bronze II] Farm - 16283 

[문제 링크](https://www.acmicpc.net/problem/16283) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

수학, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2024년 11월 2일 20:04:48

### 문제 설명

<p>목장 주인인 상배는 양과 염소들을 같이 기르고 있다. 기르는 양과 염소는 각각 한 마리 이상이다. 양과 염소는 같은 사료를 먹고, 양 한 마리는 하루에 사료를 정확히 <em>a</em> 그램 먹고, 염소 한 마리는 하루에 정확히 <em>b</em> 그램을 먹는다고 한다.</p>

<p>상배는 매일 아침 양과 염소가 각각 몇 마리인지를 확인하는 작업을 한다. 양과 염소가 각각 몇 마리인지 확인할 때, 양과 염소들이 돌아 다녀서 정확하게 그 수를 구하는 것이 쉽지 않았다. 대신에 양과 염소가 전체 몇 마리인지를 확인하고, 또 양과 염소가 어제 하루 동안 소비한 전체 사료의 양만 확인해서 양과 염소가 각각 몇 마리 인지를 알려고 한다.</p>

<p>상배가 확인한 양과 염소 전체가 <em>n</em>마리이고, 어제 하루 동안 소비한 전체 사료의 양이 <em>w</em>그램일 때, 양과 염소가 각각 몇 마리인지를 구하는 프로그램을 작성하시오. </p>

### 입력 

 <p>입력은 표준입력을 사용한다. 첫 번째 줄에 네 정수 <em>a</em>, <em>b</em>, <em>n</em>, <em>w</em>가 한 줄에 주어진다. 1 ≤ <em>a</em> ≤ 1,000, 1 ≤ <em>b</em> ≤ 1,000, 2 ≤ <em>n</em> ≤ 1,000, 2 ≤ <em>w</em> ≤ 1,000,000이다.</p>

### 출력 

 <p>출력은 표준출력을 사용한다. 첫 번째 줄에 양의 수와 염소의 수를 각각 출력한다. 만약 가능한 해가 두 개 이상 있는 경우 혹은 가능한 해가 없을 경우, -1 을 출력한다. </p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#include <string.h>

#include <stdlib.h>

int main(int argc, char* argv[])

{

	int a, b, n, w = 0;

	int ans_count = 0;
	int ans1_post = 0;
	int ans2_post = 0;
	int left = 1;
	int right = 1000;


	if (0 == scanf("%d %d %d %d", &a, &b, &n, &w))
		return 0;
	//w = 양 * a + (n - 양)b, a == b = c라면? w = 양 * c + (n-양)*c = n*c.양의 값에 상관없이 w == n*c라면 항상 참이다. 양 == 1, n-1 염소 == 1 이 아니라면? -1

	if (a == b)
	{
		if (n == 2 && a * 1 + b * 1 == w)
		{
			printf("%d %d", 1, 1);
			return 0;
		}
		else
		{
			printf("%d", -1);
			return 0;
		}

	}
	//w = 양 * a + (n - 양)b, a != b 라면? w = 양 * a + (n-양)*b, w == 양 * a - 양 * b + n*b 
	else
		for(int ans1 = 1; ans1 <= 1000; ans1++)
        {
            int cal = a*ans1 + b*(n - ans1);
            ans1 = ans1; 
            int ans2 = n - ans1;
            if(cal == w && ((1 <= ans1 && ans1 <= 1000) && (1 <= ans2 && ans2 <= 1000)))
            {
                ans_count++;
                ans1_post = ans1;
                ans2_post = ans2;
            }
        }

if(ans_count == 1)
{
    printf("%d %d", ans1_post, ans2_post);
}
else
{
printf("%d", -1);

}

	return 0;

}
```
