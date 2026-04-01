#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int max(int arr1[],int len)
{
	int max = arr1[0];
	for(int a = 0; a < len; a++)
	{
		max = max >= arr1[a] ? max : arr1[a];
		}
	
	return max;
	}
int min(int arr1[],int len)
{
	int min = arr1[0];
	for(int a = 0; a < len; a++)
	{
		min = min <= arr1[a] ? min : arr1[a];
		}
	
	return min;
}
	
int main(int argc, char *argv[])
{
	int count = 0; scanf("%d", &count);
	int* arr1; arr1 = (int*)malloc(sizeof(int) * count);
	for(int a = 0; a < count; a++)
	{
		scanf("%d", &arr1[a]);
	}
	if(count == 1)
		printf("%d", arr1[0] * arr1[0]);
	else
		{
			printf("%d", min(arr1, count) * max(arr1, count));
			}	
	
	return 0;
}