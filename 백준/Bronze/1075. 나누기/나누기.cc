#include<stdio.h>
#include<math.h>

int main(int argc, char *argv[])
{
	unsigned int N; scanf("%d", &N); N = (N / 100) * 100;
	unsigned int F; scanf("%d", &F);
//	printf("%d\n", N);
	for(unsigned int a = 0; a < 100; a++)
	{
		int temp = N + a;		
		if(temp % F == 0)
			{
				a < 10? printf("0%d", a) : printf("%d", a);
				break;
				}
		}
	

		
	return 0;
}