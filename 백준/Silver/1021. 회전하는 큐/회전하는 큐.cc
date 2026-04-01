#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int arr[50] = {0};
int N;
int len;

int ans(int now_index,int target_index, int sum)
{
   // printf("now %d target %d len %d ", now_index, arr[target_index], len);
  
    
    int sum1 = (arr[target_index] - now_index + len) % len;//정방향
    int sum2 = (now_index - arr[target_index] + len) % len;//역방향


    // 0 5 6 > wanted 5 1 >계산 결과 (5-0 +6) % 6 = 5, (0 - 5 + 6) % 6 = 1  
    
    now_index = arr[target_index];
    
    for (int a = target_index+1; a < N; a++)
    {
        arr[a] >= arr[target_index] ? arr[a]-- : arr[a];
    }
    len--;

    sum += sum1 <= sum2 ? sum1 : sum2;


   // printf("sum1 %d sum2 %d\n", sum1, sum2);

    if (target_index + 1 == N)
    {
        printf("%d", sum);
        return sum;
    }
    else {
        ans(now_index, target_index+1, sum);
    
    }


    return sum;
}






int main()
{
    scanf("%d", &len);
    scanf("%d", &N);
    for (int a = 0; a < N; a++)
    {
        scanf("%d", &arr[a]); arr[a]--;
    }

   ans(0, 0, 0);//index,target index(arr[0....N-1]), sum

    return 0;
}
