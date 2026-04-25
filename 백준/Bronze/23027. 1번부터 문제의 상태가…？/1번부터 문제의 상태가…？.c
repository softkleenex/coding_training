#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

#include<string.h>

int check_A(char message[], int len)

{

	for(int a = 0 ;a < len; a++)	{

		if(message[a] == 'A')

		{

			return 1;	

		}

	}

	return 0;	

}

int check_B(char message[], int len)

{

	for(int a = 0 ;a < len; a++)

	{

		if(message[a] == 'B')

		{

			return 1;	

		}

	}

	return 0;	

}

int check_C(char message[], int len)

{

	for(int a = 0 ;a < len; a++)

	{

		if(message[a] == 'C')

		{

			return 1;	

		}

	}

	return 0;	

}

int check(char message[], int len)

{

	if(check_A(message, len) == 1)

		return 1;

	else if(check_B(message, len) == 1)

		return 2;

	else if(check_C(message, len) == 1)

	 return 3;

	 else 

	 	return 4;

	

	

	

	}

int main() {

	char message[1001];

	scanf("%s", message);

	int index = 0;

	char temp = NULL;

	int len = 0;

	

	while (1)

	{

		if(message[len] != '\0')

			len++;

		else

		{

			break;

		}

	}

	

	

	int count = check (message, len);

	switch(count)

	{

		case(1):

	for(int a = 0; a < len; a++)

	{

		message[a] = (message[a] == 'B')||(message[a] == 'C')||(message[a] == 'D')||(message[a] == 'F') ? 'A' : message[a];

		}

		break;	

	case(2):

	for(int a = 0; a < len; a++)

	{

		message[a] = ((message[a] == 'C')||(message[a] == 'D')||(message[a] == 'F')) ? 'B' : message[a];

		}

		break;	

	case(3):

	for(int a = 0; a < len; a++)

	{

		message[a] = (message[a] == 'D')||(message[a] == 'F') ? 'C' : message[a];

		}

		break;	

	case(4):

	for(int a = 0; a < len; a++)

	{

		message[a] = 'A';

		}

		break;		

	}

	

	for(int a = 0; a < len; a++)

	{

		printf("%c", message[a]);

		}

		

		

		

	

	

return 0;

}