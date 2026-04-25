//https://www.acmicpc.net/problem/8974

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

int sum(int a)

{ //intput a, >return 1+2... +a;

	int sum = 0;	for (int i = 0; i <= a; i++)

	{

		sum += i;

	}

	return sum;

}

int main()

{

	int A, B;

	scanf("%d %d", &A, &B);

	int *arr = (int *)malloc(sizeof(int) * (B + 100)); //0 ~ B

	//0 1 2 2 3 3 3 4 4 4 4 5 5 5 5...

	int k = 0;

	for (int index = 0; index <= B + 1; index++)

	{

		arr[index] = k;

		if (index == sum(k)) //

		{

			k++;

		}

	}

	//0 > 0, 1 > 1, 1+1 > 2, 1+2 > 2, 1+2 + 1 > 3,,,,, 1+2+3 > 3, ,,,, 0+1+2+3+4 > 4,,,,

	for (int a = 0; a <= B; a++)

	{

		//		printf("%d  ", arr[a]);

		//		if(a == B) printf("\n");

	}

	int ans = 0;

	for (int a = A; a <= B; a++)

	{

		ans += arr[a];

	}

	printf("%d", ans);

	return 0;

}