#include<stdio.h>

#include<stdlib.h>

#include<string.h>

int check(int a, int b, int c)

{

	int i = a > b ? a : b;	i = i > c ? i : c;

	int other = a + b + c - i;

	

	if(other <= i)

	{

			printf("invalid!");

			return 0;

	}

	return 1;

}

void ans()

{

	int a, b, c = 0; scanf("%d %d %d", &a, &b, &c);

	

	if(0 == check(a, b, c)) return ;

	

	else if(a == b && b == c && c == a)//all same

	{

		printf("equilateral");

		}

	else if(a == b || b == c || c == a)//only two same

	{

		printf("isosceles");

		}		

	else//noting same

	{

		printf("scalene");

		}	

	}

int main(int argc, char *argv[])

{

	int t = 0; scanf("%d", &t);

	for(int i = 0; i < t; i++)

	{

		printf("Case #%d: ", i+1);

		ans();

		if (i < t -1) printf("\n");

		}

	

		

			return 0;	

}