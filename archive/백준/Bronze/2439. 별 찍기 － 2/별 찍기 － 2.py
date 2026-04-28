a = int(input())

star = "*"
empty = " "

for i in range(0, a):
    print(empty*(a-i-1) + star * (i+1))