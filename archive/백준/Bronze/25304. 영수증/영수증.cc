#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    int x; scanf("%d", &x);
    int n; scanf("%d", &n);
    int* arr1; arr1 = (int*)malloc(sizeof(int) * n);
    int* arr2; arr2 = (int*)malloc(sizeof(int) * n);

    int sum = 0;
    for(int a = 0; a < n; a++)
    {
       scanf("%d %d", &arr1[a], &arr2[a]);
        sum += arr1[a] * arr2[a];
    }
    
    if(sum != x)
        printf("No");
    else
        printf("Yes");
}
