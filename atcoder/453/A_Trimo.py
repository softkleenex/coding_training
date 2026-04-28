n = int(input())
s = input()
flag = 0
for v in s:
    if v != 'o' or flag != 0:
        print(v, end = '')
    if v != 'o':
        flag += 1
