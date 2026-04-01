# https://www.acmicpc.net/problem/5670

import sys

def solve():
    # 전체 입력을 한번에 받아서 처리 (빠른 입출력)
    data = sys.stdin.read().split()
    if not data: return
    
    idx = 0
    while idx < len(data):
        try:
            n = int(data[idx])
            idx += 1
        except IndexError:
            break
            
        words = []
        for _ in range(n):
            words.append(data[idx])
            idx += 1
            
        # Trie 구축
        root = {}
        for w in words:
            cur = root
            for char in w:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['*'] = True  # 단어 끝 표시
            
        # 클릭 수 계산
        ans = 0
        for w in words:
            cnt = 1
            cur = root[w[0]]
            for i in range(1, len(w)):
                # 분기점이거나, 현재 노드에서 끝나는 단어가 있는 경우 입력 필요
                if len(cur) > 1:
                    cnt += 1
                cur = cur[w[i]]
            ans += cnt
            
        print(f"{ans/n:.2f}")

if __name__ == "__main__":
    solve()
