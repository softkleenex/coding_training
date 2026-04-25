#include<stdlib.h>
#include<string.h>
#include<stdio.h>

int main(int argc, char *argv[])
{

int N = 0; scanf("%d", &N);
int *arr; 
arr = (int*)malloc(sizeof(int) * N);

int top = 0;

for(int a = 0; a <N; a++)
{
	scanf("%d", &arr[a]);
}



for(int a =1; a < N; a++)
{
	if((arr[a-1] < arr[a]))
	{	
	top = a;
	}
	else
	break;
}

//printf("%d", top);

for(int a =top; a < N; a++)
{
	if((a+1 < N) && (arr[a] <= arr[a+1]))
	{
		printf("NO");
		return 0;
	}
}
printf("YES");

return 0;			
}