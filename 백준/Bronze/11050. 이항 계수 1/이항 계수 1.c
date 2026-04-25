#include<stdio.h>

int ans(int num)

{

	int temp = 1;	int ans_num = 1;

	do{

		ans_num *= temp;

		temp++;

		}while(temp <= num);

		

	return ans_num;

	}

int main(int argc, char *argv[])

{

	int N = 0; int K = 0; scanf("%d %d", &N, &K);

	printf("%d", ans(N) / (ans(K) * ans(N-K)));	

	

	return 0;	

}