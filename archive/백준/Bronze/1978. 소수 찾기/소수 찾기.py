def cow(a):
    if(a == 1):
        return 0
    
    for i in range (2, a):
        if(a % i == 0):
            return 0
        

    return 1

     


N = 0
M = []


N = int(input())



M =  list(map(int, input().split()))
    
#print(M)



answer = 0
for i in range(N):
    answer += cow(M[i])

print(answer)