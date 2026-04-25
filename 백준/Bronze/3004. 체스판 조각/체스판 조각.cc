#include<stdio.h>

#include<string.h>

#include<stdlib.h>

void ans(int cut)

{//1 2, 2*2, 2*2 +2, 6 + 3, 9+3, 12 + 3..

//0 1 / 1 2 / 2 4 / 3 6/ 4 9/ 5 12 / 6 16....

//+1/+1/+2/ +2/ +3/ +3/ +4/ +4

	int total = 0;	for(int a = 0; a <= cut; a++)

	{

		total += (a/2)+1;

	}

	printf("%d", total);

}

int main(int argc, char *argv[])

{

int N = 0; scanf("%d", &N);

ans(N);

return 0;	

}