#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int turn(int arr[], int len, int count, int* start) 
{
	//start는 비어있는 인덱스(초기값은 0), 비어있는 부분은 0,
	
	int temp = 0;
	while (1) {
		*start = (*start + 1) % len;
		if (*start == 0)
		{
			(*start)++;//index0은 무조건 무효!
		}


		if (arr[*start] != 0)
			temp++;

		if (temp == count)
			break;
	}
	
	int data = arr[*start];
	arr[*start] = 0;
	return data;
}
//[0 1 2 3 4 5 6 7] 0 ~ 7,  len은 8

int main() {
	int N; scanf("%d", &N); N++;
	int* arr = NULL; 
	arr = (int*)malloc(sizeof(int) * N);

	for (int a = 1; a < N; a++)
	{
		arr[a] = a;
	}


	

	int count = 0; scanf("%d", &count);

	int* ans = NULL;
	ans = (int*)calloc(sizeof(int), (N-1));
	int start = 0;

	for (int a = 0; a < N - 1; a++)
	{
		//printf("%d\n", ans[a]);

		ans[a] = turn(arr, N, count, &start);

		//printf("%d\n", ans[a]);
	}


	
	printf("<");
	
	for (int a = 0; a < N - 1; a++)
	{
		printf("%d", ans[a]);
		if (a < N - 2)
		{
			printf(", ");
		}
	}

	printf(">", ans[N-2]);


	return 0;
}