#include<stdio.h>

#include<string.h>

#include<math.h>

#include<stdlib.h>

//https://www.acmicpc.net/problem/5988

void check(int a)

{

	if(a % 2 == 0)	printf("even");

	else

	printf("odd");

}

	

int last(char temp[])

{

	for(int a = 0; a < 60; a++)

	{

		if (!('0' <= temp[a] && temp[a] <= '9'))

			return (temp[a-1] - '0');

		}

		printf("실패");

		return -1;

	}	

	

int main(int argc, char *argv[])

{

int arr[100];

char *temp;

temp = (char*) malloc (sizeof(char) * 61);

int N = 0; scanf("%d", &N);

for(int a = 0; a < N; a++)

{

	scanf("%s", temp);

	arr[a] = last(temp);

	}

	

	

for(int a = 0; a < N; a++)

{

	check(arr[a]);

	if(a != N-1)

	{

		printf("\n");

		}

	}

	

	

	

		

	return 0;			

}