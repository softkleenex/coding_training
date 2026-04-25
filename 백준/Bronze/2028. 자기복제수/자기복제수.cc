#include<stdlib.h>

#include<stdio.h>

#include<string.h>

int arr[20];

int n;

int degree(int data)

{

	int degree = 0;	if(data / 1000 >= 1)

	{

		degree = 10000;

		}

	else if(data / 100 >= 1)

	{

		degree = 1000;

		}

	else if(data / 10 >= 1)

	{

		degree = 100;

		}

	else if(data / 1 >= 1)

	{

		degree = 10;

		}

	return degree;

}

void check(int data)

{

	int a = (data*data) % degree(data);

	if(a == data)

		printf("YES\n");

	else

		printf("NO\n");

		

}	

	

	

int main(int argc, char *argv[])

{

	 scanf("%d", &n);

	

	for(int a = 0; a < n; a++)

	{

		scanf("%d", &arr[a]);

	}

	

		

	for(int a = 0; a < n; a++)

	{

		check(arr[a]);

	}	

	

		return 0;						

}