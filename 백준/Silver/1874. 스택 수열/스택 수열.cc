//https://www.acmicpc.net/problem/1874
#include<stdio.h>
#include<string.h>
#include<stdlib.h>



char ans[300000]; int index_ans = 0;
int* target = NULL; int len_target = 0; int index_target = 0;




int answer() {
	int num_current = 1;

	int len_stack = len_target;  int* stack = (int*)malloc(sizeof(int) * len_stack); if (stack == NULL) exit(1);
	int index_stack = -1;

	for (int i = 0; i < len_target; i++)
	{
		int num_target = target[i];
		
		while (num_current <= num_target)
		{
			stack[++index_stack] = num_current++;
			ans[index_ans++] = '+';
		}

		if (stack[index_stack] == num_target)
		{
			index_stack--;
			ans[index_ans++] = '-';
		}
		else {
			printf("NO\n");
			free(stack);
			return -1;
		}
	}


	for (int a = 0; a < index_ans; a++)
	{
		printf("%c\n", ans[a]);
	}

	free(stack);
	return 1;
}






int main() {
	if (0 >= scanf("%d", &len_target)) exit(1);
	target = (int*)malloc(sizeof(int) * len_target); if (target == NULL) exit(1);

	for (int a = 0; a < len_target; a++)
	{
		if (0 >= scanf("%d", &target[a]))
			exit(1);
	}
	
	answer();

	free(target);

	return 0;
}