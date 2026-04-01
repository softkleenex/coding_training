#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int main(int argc, char *argv[])
{
	int N = 0; scanf("%d", &N);
	
	char  ans[50];
	scanf("%s", ans);
	
	for(int a = 1; a < N; a++)
	{
		char temp[50]; scanf("%s", temp);
		for(int i = 0; i < strlen(ans); i++)
		{
			if(ans[i] != temp[i])
			{
				ans[i] = '?';
			}
		}
	}
	
	printf("%s", ans);
	
	
	return 0;
}