#include<stdio.h>

#include<string.h>

#include<stdlib.h>

void total(int base)

{

	int ans = 0;	for(int a = base; a > 0; a--)

	{

		ans += a;

		}	

	printf("%d", ans);

	}

int main(int argc, char *argv[])

{

	int in = 0;

	int try = 0;

	while(1)

	{

		scanf("%d", &in);

		try++;

		if (in == 0) break;

		

		if(try > 1)

			printf("\n");

		

		total(in);

		}

	

		

	return 0;	

}