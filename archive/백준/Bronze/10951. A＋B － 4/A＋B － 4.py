
list1 = []

try:
    while True:
        A, B = map(int, input().split())
        list1.append(A+B)
    
except EOFError:
    for i in list1:
        print(i)