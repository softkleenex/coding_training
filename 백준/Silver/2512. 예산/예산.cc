#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int getmin(int *arr, int N)
{
	int temp = arr[0];
	for (int a = 0; a < N; a++)
	{
		temp = temp >= arr[a] ? arr[a] : temp;
	}

	return temp;
}

int getmax(int* arr, int N)
{
	int temp = arr[0];
	for (int a = 0; a < N; a++)
	{
		temp = temp <= arr[a] ? arr[a] : temp;
	}

	return temp;
}


int money(int arr[], int N, int line, int M)
{
	int sum = 0;
	for (int a = 0; a < N; a++)
	{	
		sum += arr[a] > line ? line: arr[a];
	}
	return sum;
}


int main() {
	int N = 0;
	scanf("%d", &N);
	int* arr; 
	arr = (int*)malloc(sizeof(int) * N);
	
	for (int a = 0; a < N; a++)
	{
		scanf("%d", &arr[a]);
	}

	



	int M; scanf("%d", &M);
	int left = 0;
	int right = getmax(arr, N);
	int answer = 0;

	
	while (left <= right)
	{
		int mid = (left + right) / 2;
		int sum = money(arr, N, mid, M);
		if (sum <= M)
		{
			answer = mid;
			left = mid + 1;
		}else
		{
			right = mid - 1;
		}
	}


	printf("%d", answer);

	free(arr);
	return 0;
}