N, X = map(int, input().split())

list1 = []

if not(1 <= N <= 10000 and 1 <= X <= 10000):
    N, X = map(int, input().split())
    
list1 = list(map(int, input().split()))

for i in list1:
    if not(1 <= i <= 10000) or (len(list1) != N):
        list1 = list(map(int, input().split()))
        
        
for i in list1:
    if i < X:
        print(i, end = " ")