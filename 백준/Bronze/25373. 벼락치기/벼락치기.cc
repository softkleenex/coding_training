#include <stdio.h>
#include <stdlib.h>
//https://www.acmicpc.net/problem/25373

unsigned long long check(unsigned long long a)
{
	int sum = 0;
	if(a >= 7)
		return (7 * a - 21);
	else{
		for(int i = 0;  a > 0 && i < 7; i--)
		{
			sum += a;
			a--;
			}
		}	
	return sum;
}

int main(int argc, char *argv[])
{
	unsigned long long n;
	scanf("%llu", &n);
	
	unsigned long long  left = 1;
	unsigned long long right  = n;
	unsigned long long result = 0;
	
	
	while(left <= right){
		unsigned long long mid = (left + right) / 2;
		 if(n <= check(mid))
		{
			result = mid;
			right = mid - 1;
			}
		else
		{
			left = mid + 1;
		}
	}

	printf("%llu\n", result);

	return 0;
}