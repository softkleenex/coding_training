#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct card{
	int front;
	int back;
	int now;
}card;


void check(card temp[], int len, int data)
{	
	for (int a = 0; a < len; a++)
	{
		if (temp[a].now <= data)
		{
			temp[a].now = (temp[a].now == temp[a].front) ? temp[a].back : temp[a].front;
		}
	}
}

int main() {
	int N = 0; int M = 0;
	scanf("%d %d", &N, &M);//앞면, 뒷면
	
	card* cards;
	cards = (card*)malloc(sizeof(card) * N);
	
	for (int a= 0; a < N; a++)
	{
		cards[a].front = 0; cards[a].back = 0; cards[a].now = 0;
		scanf("%d %d", &cards[a].front, &cards[a].back); 
		cards[a].now = cards[a].front;
	}
	
	for (int a = 0; a < M; a++)
	{
		int data = 0; scanf("%d", &data);
		check(cards, N, data);
	}


	int sum = 0;
	for (int a = 0; a < N; a++)
	{
		sum += cards[0].now;
	}


	printf("%d", sum);



	return 0;
}