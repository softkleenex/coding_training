#include <stdio.h>

int main(int argc, char *argv[])

{

	int least = 0; 	scanf("%d", &least);

	int try = 0;

		

	while(least > 0)

	{

		if (least >= 5)

		{

			least -= 5;

			try ++;

			}

		else

		{

			least -= least;

			try++;

			}

		}

	printf("%d", try);

	

	

	return 0;

}