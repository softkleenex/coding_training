a = input().strip()

if not(len(a) <= 1000):
    a = input().strip()


b = int(input().strip())

if not(1 <= b <= len(a)):
    b = int(input().strip())
    
    
c = list(a)

print(c[b-1])