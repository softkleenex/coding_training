---
title: "[Silver IV] 덱 - 10866"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 덱 - 10866 

[문제 링크](https://www.acmicpc.net/problem/10866) 

### 성능 요약

메모리: 1156 KB, 시간: 0 ms

### 분류

구현, 자료 구조, 덱

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여덟 가지이다.</p>

<ul>
	<li>push_front X: 정수 X를 덱의 앞에 넣는다.</li>
	<li>push_back X: 정수 X를 덱의 뒤에 넣는다.</li>
	<li>pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 덱에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.</li>
	<li>front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
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
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 5 -1 0, x 0 0 0 0
// 1 2 5 > 1, 4 0 (back 0 0 x front)

int arr[10001];

int front = 0;
int back = 0;
int len = 10001;

void push_front(int data)
{
    arr[front] = data;
    front = (len + front - 1) % len;
}

void push_back(int data)
{
    back = (back + 1) % len;
    arr[back] = data;
}

void pop_front()
{
    if (front != back)
    {
        front = (front + 1) % len;
        printf("%d\n", arr[front]);
        arr[front] = 0;
    }
    else
    {
        printf("%d\n", -1);
    }
}

void pop_back()
{
    if (front != back)
    {
        printf("%d\n", arr[back]);
        arr[back] = 0;
        back = (back - 1 + len) % len;
    }
    else
    {
        printf("%d\n", -1);
    }
}

void size()
{
    int size = 0;
    size = (back - front + len) % len;
    printf("%d\n", size);
}

void empty()
{
    if (front != back)
        printf("0\n");
    else
        printf("1\n");
}

void print_front()
{
    if (front == back)
        printf("-1\n");
    else
        printf("%d\n", arr[(front + 1) % len]);
}

void print_back()
{
    if (front == back)
        printf("-1\n");
    else
        printf("%d\n", arr[back]);
}

int main()
{
    int N = 0;
    scanf("%d", &N);

    char cmd[20];

    for (int a = 0; a < N; a++)
    {
        scanf("%s", cmd);
        if (strcmp(cmd, "push_front") == 0)
        {
            int temp;
            scanf("%d", &temp);
            push_front(temp);
        }
        if (strcmp(cmd, "push_back") == 0)
        {
            int temp;
            scanf("%d", &temp);
            push_back(temp);
        }
        if (strcmp(cmd, "pop_front") == 0)
        {
            pop_front();
        }
        if (strcmp(cmd, "pop_back") == 0)
        {
            pop_back();
        }
        if (strcmp(cmd, "size") == 0)
        {
            size();
        }
        if (strcmp(cmd, "empty") == 0)
        {
            empty();
        }
        if (strcmp(cmd, "front") == 0)
        {
            print_front();
        }
        if (strcmp(cmd, "back") == 0)
        {
            print_back();
        }
    }

    return 0;
}
```
