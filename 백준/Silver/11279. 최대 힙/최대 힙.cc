#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define left(a) a*2+1
#define right(a) a*2+2
#define parent(a) a == 0 ? 0 : (a-1)/2
#define swap(a, b) {int temp = a; a = b; b = temp;}


int my_index = -1;
int arr[100000];


void printarr()
{
	printf("%d, arr:", my_index);
	for (int a = 0; a <= my_index; a++)
	{
		printf("%d ", arr[a]);
	}
	printf("\n");
}

int in_check(int now_index)
{
	if (arr[parent(now_index)] >= arr[now_index])
	{
		return 0;
	}
	else if (arr[parent(now_index)] < arr[now_index])
	{
		swap(arr[parent(now_index)], arr[now_index]);
		now_index = parent(now_index);
	}

	in_check(now_index);

	return 0;
}


void in(int term)
{
	my_index++;
	arr[my_index] = term;
	in_check(my_index);
}




int pop_check(int now_index) {
	int cases = 0;
	if (left(now_index) > my_index)
		cases = 0;
	if (left(now_index) <= my_index)
		cases = 1;
	if (right(now_index) <= my_index)
		cases = 2;

	switch (cases)
	{
	case 0:
		break;
	case 1:
		if (arr[now_index] < arr[left(now_index)])
		{
			swap(arr[now_index], arr[left(now_index)]); now_index = left(now_index);
		}
		else
		{
			return 0;
		}
		break;
	case 2:
	{
		int maxindex = (arr[left(now_index)] > arr[right(now_index)]) ? (left(now_index)) : (right(now_index));

		if(arr[now_index] < arr[maxindex])
		{
			swap(arr[now_index], arr[maxindex]);
			now_index = maxindex;
			pop_check(now_index);
		}
		else {
			return 0;
		}
		break;
	}
	default:
		break;
	}

	return 0;
}


void pop()
{
	if (my_index == -1)
	{
		printf("0\n");//제출 전에 0으로 수정
	}
	else
	{
		printf("%d\n", arr[0]);
		swap(arr[my_index], arr[0]);
		my_index--;
		pop_check(0);
	}

}

/*0
1 2
34 56
78 910 11 12
*/

int main() {
	int N; scanf("%d", &N);
	



	for (int a = 0; a < N; a++)
	{
		scanf("%d", &arr[a]);
	}

	for (int a = 0; a < N; a++)
	{
		int term = arr[a];
		switch (term)
		{
		case 0:
			//printf("pop\n");
			pop();
			//printarr();
			break;
		default:
			//printf("in\n");
			in(term);
			//printarr();
			break;
		}
	}



	return 0;
}