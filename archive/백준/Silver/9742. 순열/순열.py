# https://www.acmicpc.net/problem/9742

while 1:
    try:
        s, x = (input().split())
        s = sorted(list(str(s)))
        # print(s, x)
        
        count = 0
        ans = []
        n = len(s)
        visited = [-1 for i in range(n)]
        flag = 0
        
        def back(buck, now):
            global count
            global flag
            if len(buck) == n:
                count += 1
                if count == int(x):
                    print(f"{''.join(s)} {x} = ", end ='')
                    print("".join(buck))
                    flag = 1
                return
            if now == n:
                return
            
            for i in range(n):
                if visited[i] == -1:
                    visited[i] = 1
                    back(buck + [s[i]], now + 1)
                    visited[i] = -1


        back([], 0)
        
        if flag == 0:
            print(f"{''.join(s)} {x} = ", end ='')
            print("No permutation")
    except:
        break