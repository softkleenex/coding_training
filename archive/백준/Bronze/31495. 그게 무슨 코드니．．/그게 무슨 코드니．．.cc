#include<stdio.h>

#include<string.h>

#include<stdlib.h>

void check(char sen[])

{

int sen_len = strlen(sen);	if(sen[0] == '"' && sen[sen_len -1] == '"' && sen_len > 2)

	{

		sen[sen_len-1] = '\0';

		printf("%s", &(sen[1]));

	}

	else

		printf("CE");

	

	}

int main(int argc, char *argv[])

{

	char sen[51] = "0";

	scanf("%[^\n]",  sen);

//	printf("%s", sen);

	check(sen);

	

	

	

	return 0;

}