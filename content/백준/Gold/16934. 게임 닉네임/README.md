---
title: "[Gold III] 게임 닉네임 - 16934"
tags: ["백준", "Gold III"]
---

# [Gold III] 게임 닉네임 - 16934 

[문제 링크](https://www.acmicpc.net/problem/16934) 

### 성능 요약

메모리: 237700 KB, 시간: 688 ms

### 분류

자료 구조, 문자열, 트리, 집합과 맵, 해시를 사용한 집합과 맵, 트라이

### 제출 일자

2025년 9월 21일 16:14:59

### 문제 설명

<p>스타트링크에서 매우 재미있는 게임을 만들었다. 이 게임은 정말 재미있다.</p>

<p>게임에는 유저가 접속하는 기능이 있고, 각 유저는 가입할 때, 자신의 닉네임을 정해야 한다. 닉네임은 알파벳 소문자로만 이루어져 있고, 두 유저가 같은 닉네임을 정하는 것도 가능하다.</p>

<p>이 게임은 유저의 닉네임을 이용해서 내부에 저장할 별칭을 만든다. 별칭은 유저에게 보여지지는 않고, 내부에서만 사용된다. 저장 공간을 최소로 하기 위해서 별칭의 길이를 최소로 하려고 한다.</p>

<p>별칭은 유저 닉네임의 접두사(Prefix) 중에서 가장 길이가 짧은 것을 사용한다. 이때, 접두사가 이전에 가입한 닉네임의 접두사가 아니어야 한다. 가능한 별칭이 없는 경우에는 유저가 가입한 시점까지 같은 닉네임으로 가입한 사람의 수 x를 계산해야 한다. x가 1인 경우에는 닉네임을 별칭으로 사용하고, x가 2 이상인 경우에는 닉네임의 뒤에 x를 붙여서 별칭으로 사용한다.</p>

<p>예를 들어, 닉네임을 "baekjoon"으로 정한 유저가 가입하면, 이 유저의 별칭은 "b"가 된다. </p>

<p>그 다음, 닉네임이 "startlink"로 정한 유저가 가입하면, 이 유저의 별칭은 "s"이다. "bakejoon"이 닉네임인 유저가 가입하면, 별칭은 "bak"가 되고, "beakjoon"인 유저가 가입하면, 별칭은 "be"가 된다. 마지막으로 "baekjoon"으로 유저가 가입하면 별칭은 "baekjoon2"가 된다.</p>

<p>유저가 가입한 순서대로 닉네임이 주어졌을 때, 각 유저의 별칭을 구해보자. 위의 규칙을 이용해 별칭을 정하면 두 유저가 같은 별칭을 갖는 것도 가능하다.</p>

### 입력 

 <p>첫째 줄에 가입한 유저의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 유저의 닉네임이 가입한 순서대로 한 줄에 하나씩 주어진다. 닉네임은 알파벳 소문자로만 이루어져 있고, 길이는 10을 넘지 않는다.</p>

### 출력 

 <p>유저가 가입한 순서대로 별칭을 한 줄에 하나씩 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/16934


class Node(object):
    def __init__(self, key, data=None):
        self.key = key #값으로 입력될 문자
        self.data = data #문자열의 종료를 알리는 flag
        self.children = {} #자식노드를 저장

class Trie:
    def __init__(self): #head를 빈 노드로 저장
        self.head = Node(None)
        self.nickname_count = {}  # 닉네임별 등장 횟수

    def insert(self, string): #트리를 생성하는 함수
        current_node = self.head #self.head라는 존재하는 - 클래스 선언시에 자동으로 만들어지는 - 객체와 currnet_node를 얕은 복사

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
                return False

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                    break
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
    


t = int(input())

trie = Trie()

for _ in range(t):
    temp = input().strip()
    shortest_t = temp
    
    for x in range(len(temp)):
        if trie.starts_with(temp[0:x + 1]) == False:
            shortest_t = temp[0 :x + 1]
            break
        else:
            pass
    
    ans_t = shortest_t
    # print(shortest_t, 'n')

    
    
    if temp in trie.nickname_count:
        trie.nickname_count[temp] += 1
        ans_t = temp + str(trie.nickname_count[temp])
    else:
        trie.insert(temp)
        trie.nickname_count[temp] = 1
       
    
    print(ans_t)
        
    


```
