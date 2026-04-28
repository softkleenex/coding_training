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