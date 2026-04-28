#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


void sort(int arr[], int len, int try)
{
	int index_last = len-1;

	for (int a = 0; a < try; a++)
	{
		int index_max = 0;
		for (int b = 0; b <= index_last; b++)
		{
			index_max = arr[index_max] > arr[b] ? index_max : b;
		}

		int max = arr[index_max];
		arr[index_max] = arr[index_last];
		arr[index_last] = max;
		index_last == index_max ? try++ : try;//미교관시에 try 보정
		index_last--;
		if (index_last == -1)
		{
			printf("-1"); exit(0);
		}



	}



	for (int a = 0; a < len; a++)
	{
		printf("%d", arr[a]);
		if (a < len - 1)
			printf(" ");
	}


	//arr print
}

int main() {
	int len = 0; scanf("%d", &len);
	int try = 0; scanf("%d", &try);
	int* arr1 = (int*)malloc(sizeof(int) * len);


	for (int a = 0; a < len; a++)
	{
		scanf("%d", &arr1[a]);
	}
	
	sort(arr1, len, try);

	return 0;
}