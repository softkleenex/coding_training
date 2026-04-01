#include<stdio.h>

int main(int argc, char *argv[])
{
int N = 0; scanf("%d", &N);

int ans = 1;
for(int a = 1; a <= N; a++)
{
ans *= a;	
	}
	printf("%d", ans);
	
	
	return 0;
	
		
				
}