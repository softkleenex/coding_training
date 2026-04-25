list1 = []
A = 1
B = 1

while True:
        A, B = map(int, input().split())
        
       
        if A ==0 and B ==0:
            break
       
        if not (0 < A < 10 and 0 < B < 10):
            A, B = map(int, input().split())
        
       
        
        
        list1.append(A+B)


for i in list1:
        print(i)