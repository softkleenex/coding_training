# https://www.acmicpc.net/problem/2744

x = input()

for x1 in x:
    if x1.isupper():
        print(x1.lower(), end = '')
    else:
        print(x1.upper(), end = '')