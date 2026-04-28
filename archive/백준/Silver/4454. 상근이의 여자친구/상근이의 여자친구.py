# https://www.acmicpc.net/problem/4454

while 1:
    try:
        a, b, c, d, m, t  = map(float, input().split())
  
        v = 0
        l = 0
        r = 10000000
        for _ in range(1000):
            v = (l + r) / 2
            oil = (a * (v ** 4) + b * (v **3) + c * (v ** 2) + d * v) * (m / v)
            if  t <= oil: #소모된오일이 더 많은경우
                r = v
            elif t > oil:#오일이 남은경우
                l = v   
        v = int(v * 100) / 100
        print(f"{v:.2f}")
    except:
        break