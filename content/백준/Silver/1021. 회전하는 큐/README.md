---
title: "[Silver III] 회전하는 큐 - 1021"
tags: ["백준", "Silver III"]
---

# [Silver III] 회전하는 큐 - 1021 

[문제 링크](https://www.acmicpc.net/problem/1021) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

자료 구조, 덱

### 제출 일자

2024년 10월 14일 20:12:47

### 문제 설명

<p>지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.</p>

<p>지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.</p>

<ol>
	<li>첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a<sub>1</sub>, ..., a<sub>k</sub>이었던 것이 a<sub>2</sub>, ..., a<sub>k</sub>와 같이 된다.</li>
	<li>왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>2</sub>, ..., a<sub>k</sub>, a<sub>1</sub>이 된다.</li>
	<li>오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>k</sub>, a<sub>1</sub>, ..., a<sub>k-1</sub>이 된다.</li>
</ol>

<p>큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 문제의 정답을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int arr[50] = {0};
int N;
int len;

int ans(int now_index,int target_index, int sum)
{
   // printf("now %d target %d len %d ", now_index, arr[target_index], len);
  
    
    int sum1 = (arr[target_index] - now_index + len) % len;//정방향
    int sum2 = (now_index - arr[target_index] + len) % len;//역방향


    // 0 5 6 > wanted 5 1 >계산 결과 (5-0 +6) % 6 = 5, (0 - 5 + 6) % 6 = 1  
    
    now_index = arr[target_index];
    
    for (int a = target_index+1; a < N; a++)
    {
        arr[a] >= arr[target_index] ? arr[a]-- : arr[a];
    }
    len--;

    sum += sum1 <= sum2 ? sum1 : sum2;


   // printf("sum1 %d sum2 %d\n", sum1, sum2);

    if (target_index + 1 == N)
    {
        printf("%d", sum);
        return sum;
    }
    else {
        ans(now_index, target_index+1, sum);
    
    }


    return sum;
}






int main()
{
    scanf("%d", &len);
    scanf("%d", &N);
    for (int a = 0; a < N; a++)
    {
        scanf("%d", &arr[a]); arr[a]--;
    }

   ans(0, 0, 0);//index,target index(arr[0....N-1]), sum

    return 0;
}

```
