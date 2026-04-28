line1 = []

while True:
    try:
        line2 = list(map(int, input().split()))

        if not(1 <= line2[0] <= 10000, 1<= line2[1] <= 10**9):
            line2 = map(int, input().split())
        
        line2[0] = line2[0] + 1
        
        if(line2[1] % line2[0] == 0):
            line1.append(line2[1] // line2[0])
        else :
            line1.append(line2[1] // line2[0])
        
    except EOFError:
        break


for i in line1:
    print(i)


