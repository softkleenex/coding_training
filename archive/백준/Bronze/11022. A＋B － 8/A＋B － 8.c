#include<stdio.h>



int main(int argc, char *argv[])
{
	int T = 0;
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
	{
		int a = 0; int b = 0;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d", i,  a, b, a+b);
		if(i != T) printf("\n");
		}
	
	
	
	
	return 0;
}