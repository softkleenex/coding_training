N, M = map(int, input().split())
           
while not (0 <= N <= 100 and 0 <= M <= 100):
    N, M = map(int, input().split())
    
A = []
B = []  
    
for i in range(N):
       temp = list(map(int, input().split()))
       for i in range(M):
           if not(temp[i] <= 100 and temp[i] >= -100):
                temp = list(map(int, input().split()))

       A.append(temp[0:M])
       
       

for i in range(N):
    temp2 = list(map(int, input().split()))
    for i in range(M):
        if not(temp[i] <= 100 and temp[i] >= -100):
            temp2 = list(map(int, input().split()))
            
    B.append(temp2[0:M])
   
   
c = []

for i in range(N):
    for k in range(M):
        c.append(A[i][k] + B[i][k])



for i in range(N):
    if (i != 0):
        print("")
    for k in range(M):
       print(c[i*M + k],"", end= '')
