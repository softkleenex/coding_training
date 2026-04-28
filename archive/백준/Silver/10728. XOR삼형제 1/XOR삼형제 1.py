# https://www.acmicpc.net/problem/10728

import collections
import itertools
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    max_len = 0
    max_list = []
    
    def back(now_num, buck, visited):
        global max_len, max_list
        left = n - now_num + 1
        
        if(len(buck) + (left)) <= max_len:
                return
        
        if now_num > n:
            if len(buck) > max_len:
                max_len = len(buck)
                max_list =  buck.copy()
            return

        #우주1: 현재 숫자를 내 바구니에 "넣는" 경으
        
        if not now_num in visited:
            new_visited = visited.copy()
            
            for numbuck in buck:
                new_visited.add(numbuck ^ now_num)
            
            buck.append(now_num)
            
            #바구니에 넣은 상태로 다음 숫자 검사하러 떠나기
            
            back(now_num + 1, buck, new_visited)
            
            #탐색을 끝내고 돌아왔으면, 다른 경우 탐색을 위해서 방금 넣었던것을 다시 뺀다!
            
            buck.remove(now_num)
            
        #우주 2 현재 숫자를 내 바구니에 넣지않고 버리는 경우
        #바구니랑 금지목록은 그대로, 번호만 넘긴다
        
        back(now_num + 1, buck, visited)
                
    back(1, [], set())
    print(max_len)
    print(*max_list)
            
        
            
    