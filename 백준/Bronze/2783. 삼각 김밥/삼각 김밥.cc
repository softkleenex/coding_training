#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
	float X, Y; 
	scanf("%f %f", &X, &Y);
	float min = (X *1000)/Y;//1000그램의 가격은? 
	
	int N ; scanf("%d", &N);
	
	
	for(int a = 0; a < N; a++)
	{
		int prize,count;
		scanf("%d %d", &prize, &count);
		min = ((min < (float)(prize*1000)/count) ? min :  (float)(prize*1000)/count);
		}

	printf("%f", min);


	return 0;
}