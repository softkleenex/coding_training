#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int ans(int N, int K)
{

	for (int a = 1; a <= N; a++)
	{
		if (N % a == 0)
		{
			K--;
		}
		if (K == 0)
		{
			printf("%d", a);
			return 0;
		}
	}
	
	printf("0");
	return 0;



}

int main() {
	int N = 0; int K = 0; scanf("%d %d", &N, &K);
	ans(N, K);
	return 0;
}