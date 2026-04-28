---
title: "[Silver IV] 스택 - 10828"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 스택 - 10828 

[문제 링크](https://www.acmicpc.net/problem/10828) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

구현, 자료 구조, 스택

### 제출 일자

2024년 5월 28일 20:44:49

### 문제 설명

<p>정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 다섯 가지이다.</p>

<ul>
	<li>push X: 정수 X를 스택에 넣는 연산이다.</li>
	<li>pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 스택에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 스택이 비어있으면 1, 아니면 0을 출력한다.</li>
	<li>top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
</ul>

### 입력 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### 출력 

 <p>출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.</p>



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

// 스택 구조체 정의
typedef struct
{
    int *data; // 스택 데이터를 저장할 배열
    int top;   // 스택의 최상위 원소의 인덱스
} stack;

stack *init()
{
    stack *stacks = (stack *)malloc(sizeof(stack));
    stacks->data = (int *)calloc(10000, sizeof(int));
    stacks->top = -1;
    return stacks;
}

// 정수 X를 스택에 넣는 연산이다.
void push(stack *stacks, int x)
{
    stacks->data[stacks->top + 1] = x;
    (stacks->top)++;
}

// 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
// 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop(stack *stacks)
{
    if (stacks->top != -1)
    {
        printf("%d\n", stacks->data[stacks->top]);
        stacks->data[stacks->top] = -1;
        stacks->top--;
    }
    else
        printf("-1\n");
}

// 스택에 들어있는 정수의 개수를 출력한다.
void size(stack *stacks)
{
    printf("%d\n", stacks->top + 1);
}

// 스택이 비어있으면 1, 아니y면 0을 출력한다.
void empty(stack *stacks)
{
    if (stacks->top != -1)
        printf("0\n");
    else
        printf("1\n");
}

// 스택의 가장 위에 있는 정수를 출력한다.
// 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void top(stack *stacks)
{
    if (stacks->top != -1)
        printf("%d\n", stacks->data[stacks->top]);
    else
        printf("%d\n", -1);
}

int main()
{

    int N = 0;

    stack *stacks = init();

    scanf("%d", &N);

    int command[10000] = {-1};
    int push_arr[10000] = {-1};
    int push_count = 0;

    for (int a = 0; a < N; a++)
    {
        char temp1[10];
        scanf("%s", temp1);

        if (0 == strncmp(temp1, "push", 4))
        {
            command[a] = 0;
            scanf("%d", &push_arr[push_count]);
            push_count++;
        }
        else if (0 == strncmp(temp1, "pop", 3))
        {
            command[a] = 1;
        }
        else if (0 == strncmp(temp1, "size", 4))
        {
            command[a] = 2;
        }
        else if (0 == strncmp(temp1, "empty", 5))
        {
            command[a] = 3;
        }
        else if (0 == strncmp(temp1, "top", 3))
        {
            command[a] = 4;
        }
    }
    push_count = 0;
    for (int a = 0; a < N; a++)
    {

        switch (command[a])
        {
        case (0):
        {
            push(stacks, push_arr[push_count]);
            push_count++;
            break;
        }
        case (1):
        {
            pop(stacks);
            break;
        }
        case (2):
        {
            size(stacks);
            break;
        }
        case (3):
        {
            empty(stacks);
            break;
        }
        case (4):
        {
            top(stacks);
            break;
        }
        default:
        {

            break;
        }
        }
    }
}
```
