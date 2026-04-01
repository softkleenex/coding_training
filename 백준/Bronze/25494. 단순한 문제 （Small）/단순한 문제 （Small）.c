#include<stdio.h>

void ans(int a, int b, int c)

{

	int count = 0;	for(int i1 = 1; i1 <= a; i1++)

	{

		for(int i2 = 1; i2 <= b; i2++)

		{

			for(int i3 = 1; i3 <= c; i3++)

			{

				if(i1 % i2 == i2 % i3 && i2 % i3 == i3 % i1)

				{

					count++;

					}

				}	

			}		

		}

	printf("%d", count);

	

	}

int main(int argc, char *argv[])

{

int t = 0; scanf("%d",  &t);

for(int i = 0; i < t; i++)

{

	int a, b, c= 0; scanf("%d %d %d", &a, &b, &c);

	ans(a, b, c);

	if(i < t-1)	printf("\n");

}

		

	return 0;			

}