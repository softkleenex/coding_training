#include <stdio.h>
#include <stdlib.h>

///https://www.acmicpc.net/problem/16951

int block(int start, int N, int tow[], int K)
{
	int mintime = 0;
	int temptime = 0;

	int temptow[1001];
	for (int a = 0; a < 1001; a++)
	{
		temptow[a] = tow[a];
	}

	for (int a = 1; a <= 1000; a++)
	{
		if (temptow[0] != a)
		{
			temptow[0] = a;
			temptime++;
		}
		for (int b = 1; b < N; b++)
		{
			if (temptow[b] != temptow[b - 1] + K)
			{
				temptow[b] = temptow[b - 1] + K;
				temptime++;
			}
		}

		if (a == 1 || mintime > temptime)
		{
			mintime = temptime;
		}

		temptime = 0;
		for (int a = 0; a < 1001; a++)
		{
			temptow[a] = tow[a];
		}
	}

	return mintime;
}

int main(int argc, char *argv[])
{
	int tow[1001] = {-1};

	int N = 0;
	int K = 0;

	scanf("%d", &N);
	scanf("%d", &K);

	for (int a = 0; a < N; a++)
	{
		scanf("%d", &tow[a]);
	}

	printf("%d", block(0, N, tow, K));

	return 0;
}