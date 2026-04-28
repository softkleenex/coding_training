---
title: "[Bronze II] 수 정렬하기 - 2750"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 수 정렬하기 - 2750 

[문제 링크](https://www.acmicpc.net/problem/2750) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

정렬, 구현

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include<stdio.h>
#include<stdlib.h>
//insertions sort
/*
Algorithm(다음을 반복 실행)
/ 크기 순으로 정렬된 길이 i의 array에 i+1번째 숫자를 삽입
Complexity
O(n2): Worst/Average Case
O(n): Best Case

*/



//selection sort
/*
Algorithm(하나의 원소가 남을 때 까지 다음을 반복 실행)
1. 리스트의 최대 원소를 찾는다.
2. 최대 원소와 맨 오른쪽 원소를 교환한다.
3. 맨 오른쪽 원소 제외

*/

/*
N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
*/

int main(int argc, char *argv[])
{
 	int N = 0;
 	scanf("%d", &N);
 	
 	int* arr = (int*)malloc(sizeof(int)*N);
 	
 	for(int a = 0; a < N; a++)
 	{
 		scanf("%d", &arr[a]);
 	}
 	
// //샵입정렬 - insertions sort
// 	for(int a = 1; a < N; a++)
//{
//	for(int b = 0; b < a; b++)
//	{
//		if(arr[a]<= arr[b])
//		{
//		//arr[a]를 arr[b]자리에 넣어야 함
//			int t1 = arr[b];
//			int t2 = arr[a];
//			
//			for(int c = a-1; c >= b; c--)
//			{
//			arr[c+1] = arr[c];
//			
//			//arr[a] = arr[a-1]
//			//arr[b+1] = arr[b]	
//			}
//			arr[b] = t2;
//		
//			break;
//				
//		}
//	}
//}

//선택정렬 - selection sort
for(int k = N-1; k >0; k--){
	
	int max = arr[0];
	int max_index = 0;	
	
	for(int a = 1; a <= k; a++)
	{
		max_index = arr[a] > max? a : max_index ;
		max = arr[a] > max? arr[a] : max ;
	}	
	int t = arr[k];
	arr[k] = max;
	arr[max_index] = t;
}
  
 for(int a = 0; a < N; a++)
 	{
 		printf("%d\n", arr[a]);
 	}


 	free(arr); 	
 	return 0;
}
```
