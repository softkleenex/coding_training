a = int(input())
if not(1 <= a <= 100):
    a = int(input())
list1 = []


list1 = list(map(int, input()))
if len(list1) != a:
    list1 = list(map(int, input()))

sum = 0    
for i in list1:
    sum += i
    
    
print(sum)