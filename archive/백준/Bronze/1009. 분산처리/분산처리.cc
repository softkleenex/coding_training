#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>



int main() {
	int N; scanf("%d", &N);
	int* test; 
	test = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		int temp = 1;
		for (int k = 0; k < b; k++)
		{
			temp = (temp * a) % 10;
		}
		int ans = temp % 10;
		test[i] = ans;
	}

	for (int i = 0; i < N; i++)
	{
		test[i] == 0 ? test[i] = 10 : test[i];
		printf("%d\n", test[i]);
	}


	return 0;
}