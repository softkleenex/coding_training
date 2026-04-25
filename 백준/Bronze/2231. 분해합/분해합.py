def creat(a):
    b = 1
    c = []
    while True:
        d = b
        while not d == 0:
            # print(d)
            e = d % 10
            c.append(e)
            d = d // 10
        if(a == b + sum(c)):
            print(b)
            break
        if (1000000 <=b):
            print("0")
            break
        c.clear()
        b = b + 1
        
        
        
while True:        
    a = int(input())
    if  1 <= a <= 1000000:
        break


creat(a)
