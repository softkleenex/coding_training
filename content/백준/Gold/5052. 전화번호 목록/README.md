---
title: "[Gold IV] 전화번호 목록 - 5052"
tags: ["백준", "Gold IV"]
---

# [Gold IV] 전화번호 목록 - 5052 

[문제 링크](https://www.acmicpc.net/problem/5052) 

### 성능 요약

메모리: 233284 KB, 시간: 924 ms

### 분류

자료 구조, 문자열, 정렬, 트리, 집합과 맵, 트라이

### 제출 일자

2025년 9월 17일 18:43:51

### 문제 설명

<p>전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.</p>

<p>전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.</p>

<p>예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자</p>

<ul>
	<li>긴급전화: 911</li>
	<li>상근: 97 625 999</li>
	<li>선영: 91 12 54 26</li>
</ul>

<p>이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다. </p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 t가 주어진다. (1 ≤ t ≤ 50) 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. (1 ≤ n ≤ 10000) 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다. 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/5052
# coderefer https://m.blog.naver.com/cjsencks/221740232900

class Node(object):
    def __init__(self, key, data=None):
        self.key = key #값으로 입력될 문자
        self.data = data #문자열의 종료를 알리는 flag
        self.children = {} #자식노드를 저장

class Trie:
    def __init__(self): #head를 빈 노드로 저장
        self.head = Node(None)

    def insert(self, string): #트리를 생성하는 함수
        current_node = self.head

        for char in string: 
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string): #문자열이 존재하는지에 대한 여부를 리턴하는 함수입니다. 문자열을 하나씩 돌면서 확인 후 ​마지막 노드가 data가 존재한다면 True를, 그렇지 않거나 애초에 children에 존재하지 않는다면 False를 리턴합니다.
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix): #prefix단어로 시작하는 단어를 찾고 배열로 리턴하는 함수입니다. prefix단어까지 tree를 순회 한 이후 그다음부터 data가 존재하는 것들만 배열에 저장​하여 리턴합니다.
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
    
    
t = int(input())

for _ in range(t):
    n = int(input())
    now_numbers = list()
    
    for __ in range(n):
        now_numbers.append(input().strip())
    
    trie = Trie()
    word_list = now_numbers.copy()
    for word in word_list:
        trie.insert(word)
    
    ans = True
    for nowword in word_list:
        if  ( len(trie.starts_with(nowword)) == 1):
            pass
        else:
            ans = False
    

    print("YES") if ans == True else print("NO")
```
