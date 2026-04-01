#include<math.h>
#include<stdio.h>





int main() {
	int try = 0; scanf("%d", &try);
	for (int a = 0; a < try; a++)
	{
		int A = 0; int B = 0;
		scanf("%d %d", &A, &B);
		printf("%d\n", (A*A) / (B*B));
	}



	return 0;
}