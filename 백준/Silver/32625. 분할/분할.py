

n = int(input())
a = list(map(int, input().split()))


#크기 1에서 N-1 // 2 까지 분할해보며 구간 검색을 하면? > (N / 2) ^ 2 > 5000000000 50억인디 ;
#일단 해보자

for i in range(1, (n) // 2 + 1):
    if n % i == 0:
        ans = sum(
            (
                min(a[0*i :0 * i + i]), max(a[0*i :0 * i + i])
                    )
                )
            
        if all(ans == 
               sum(
                   [min(a[i2*i :i2 * i + i]), 
                   max(a[i2*i :i2 * i + i])]
                   ) for i2 in range(n) if i2 * i + i <= n):
        #만약 i 가 3이라면 a[0 : 3] a [3 : 6] a [6 : 9]
            print(1)
            quit()
            
print(0)