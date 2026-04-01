 #include <stdio.h>

#include <string.h>

#include <stdlib.h>

void friend_2nd(int d[50][50], int len) {

 	 for(int m=0; m < len; m++)

   	 	for(int s=0; s < len; s++)

    	  	for(int e = 0; e < len; e++)

      	  		if (s != m && m != e && e != m)

							if(d[s][e] > d[s][m] + d[m][e]) d[s][e] = d[s][m] + d[m][e];

}

int main(){

	int N = 0; scanf("%d",  &N);

	int friends [50][50] = {0};

	for(int a = 0; a <N; a++)

	{

		for(int a2 = 0; a2 < N; a2++)

		{

			char temp = '0';

			scanf(" %c", &temp); 

			friends[a][a2] = (temp == 'Y') ? 1 : 999999;

			}

		}

		

	friend_2nd(friends, N);

	

	int max = 0;

	for(int i = 0; i < N; i++)

		{

			int count = 0;

			for(int j = 0; j < N; j++)

				{

					if(i != j && friends[i][j] <= 2) count++;

					}

				max = max >= count ? max : count;

			}

	

	printf("%d", max);

	

	

	

	return 0;

	}