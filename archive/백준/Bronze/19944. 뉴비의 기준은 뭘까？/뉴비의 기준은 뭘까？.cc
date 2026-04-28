#include<stdio.h>

int main(int argc, char *argv[])

{

	int N = 0; int M = 0; scanf("%d %d", &N, &M);	if(M <= 2)	

		printf("NEWBIE!");

	else if(2 < M && M <= N)

		printf("OLDBIE!");

	else

		printf("TLE!");

	

	

	

	return 0;

}