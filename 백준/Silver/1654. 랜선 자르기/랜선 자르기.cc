#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#include <math.h>

#include <limits.h>

long long K;

long long *arr1;

long long N;

long long ans(long long left, long long right, long long postlen)

{

	long long mid = (left + right) / 2;	long long now_lencount = 0;

	long long next_len = postlen;

		for (long long a = 0; a < K; a++)

		{

			now_lencount += arr1[a] / mid;

			//현재 값으로 arr[a]를 통해 만들어지는 랜선의 개수 구하기!

		}

	

	

	if (now_lencount >= N) //갯수 충족시에

	{

		if(postlen > mid)//전의 길이보다 적으면?

			{

				left = mid+1;//더 길게 try

				next_len = postlen;				

			}

		else if(postlen < mid)//전의 길이보다 크면?

			{

				left = mid+1;//더 길게 try

				next_len = mid;

			}

	}

	else if (now_lencount < N) //갯수 미충족

	{//짧게 try

		right = mid-1;

		next_len = postlen;

	}

	//현 단게 ans기반 left right 조정 끝

	

	//재귀 여부를 결정하자!

	if (left > right)//종료

	{

		printf("%lld", next_len);//가장 최적의 lens출력

		return mid;

	}

	else

	{

		return (ans(left, right, next_len));

	}

	return 0;

}

int main(int argc, char *argv[])

{

	scanf("%lld", &K); //보유 랜선 개수

	scanf("%lld", &N); //필요 랜선 개수

	arr1 = (long long *)malloc(sizeof(long long) * K);

	long long min_len = 1; //최소 길이

	long long max_len = 0; //최대 길이(K개의 랜선중에 가장 큰길이

	for (long long a = 0; a < K; a++)

	{

		scanf("%lld", &arr1[a]);

	}

	for (long long i = 0; i < K; i++)

	{

		max_len = (max_len > arr1[i]) ? (max_len) : (arr1[i]);

	}

	ans(min_len, max_len, 0); //1 ~ max로 이분탐색 시행 - N와 랜선 길이 범위가 매우 크다!

	

	free(arr1);

	return 0;

}