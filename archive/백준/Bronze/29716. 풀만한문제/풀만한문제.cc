#include <stdio.h>
#include <stdlib.h>

int check(char arr[])
{
	int sum = 0;
	for (int a = 0; arr[a] != '\0'; a++)
	{
		if (('A' <= arr[a] && arr[a] <= 'Z'))
			sum += 4;
		else if (('0' <= arr[a] && arr[a] <= '9') || ('a' <= arr[a] && arr[a] <= 'z'))
			sum += 2;
		else if (' ' == arr[a])
			sum += 1;
	}
	return sum;
}

	int main(int argc, char *argv[])
	{
		int J, N;
		scanf("%d %d", &J, &N);
		char arr1[100];
		int ans = 0;
		for (int a = 0; a < N; a++)
		{
			scanf(" %[^\n]", arr1);
			if(J >= check(arr1)) 
				ans++;
		}
		printf("%d", ans);
		
		return 0;
		
	}