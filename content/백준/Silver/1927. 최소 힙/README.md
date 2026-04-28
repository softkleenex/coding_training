---
title: "[Silver II] 최소 힙 - 1927"
tags: ["백준", "Silver II"]
---

# [Silver II] 최소 힙 - 1927 

[문제 링크](https://www.acmicpc.net/problem/1927) 

### 성능 요약

메모리: 1896 KB, 시간: 20 ms

### 분류

자료 구조, 우선순위 큐

### 제출 일자

2024년 4월 25일 17:34:17

### 문제 설명

<p>널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.</p>

<ol>
	<li>배열에 자연수 x를 넣는다.</li>
	<li>배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.</li>
</ol>

<p>프로그램은 처음에 비어있는 배열에서 시작하게 된다.</p>

### 입력 

 <p>첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. x는 2<sup>31</sup>보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.</p>

### 출력 

 <p>입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define swap(a, b) do{int temp = a; a = b; b = temp;}while(0)

int heap[100000];
int size = 0;



int parent(int index)
{ 
    return (index -1) /2;
}

int leftChild(int index)
{ 
    return (index)*2 +1;
}

int rightChild(int index)
{ 
    return (index)*2 + 2;
}


void insert(int value)
{
    if (size == 9999)
    {}    //힙이 꽉 찼다
    
    int index = size;
    heap[size] = value;
    size ++;
    
    while ((index != 0) && (heap[parent(index)] > heap[index]))
    {
        swap(heap[index], heap[parent(index)]);
        index = parent(index);
    }
}




void minHeapify(int index)
{
    int left = leftChild(index);
    int right = rightChild(index);
    int smallest = index;

    if (left < size && heap[left] < heap[smallest])
        smallest = left;
    if(right < size && heap[right] < heap[smallest])
        smallest = right;
    
    if (smallest != index)
    { 
        swap(heap[index], heap[smallest]);
        minHeapify(smallest);
    }

}

int removeMin()
{
    if (size <= 0)
        return 0;
    
    if (size == 1)
    {
        size -= 1;
        return heap[0];
    }

    int root = heap[0];
    heap[0] = heap[size -1];
    size -= 1;
    minHeapify(0);

    return root;

}




int main()
{
int n = 0;
scanf("%d", &n);



int* arr2 = malloc(sizeof(int) * (size_t)n);

for(int a = 0; a < n; a ++)
{
    scanf("%d", &arr2[a]);
}

for(int a = 0; a < n; a++)
{
int x = 0;
x = arr2[a]; 
//0 입력시 배열의 최소값 출럭, 그 배열 제거 
// 자연수 입력시에 배열에 그 값 넣음

    if(x == 0)
    {
        if(size == 0) //인덱스가 0 >> 즉, 배열이 아예 비워져 있는 경우
            printf("0\n");
        else//배열에 뭐라도 있는 경우
        {   
            printf("%d\n", heap[0]);
            removeMin();
        }
    }
    if(x > 0)
    {
       insert(x);
    }
}


return 0;

}
```
