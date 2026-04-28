---
title: "[Silver I] 트리 순회 - 1991"
tags: ["백준", "Silver I"]
---

# [Silver I] 트리 순회 - 1991 

[문제 링크](https://www.acmicpc.net/problem/1991) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

트리, 재귀

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="" style="height:220px; width:265px"></p>

<p>예를 들어 위와 같은 이진 트리가 입력되면,</p>

<ul>
	<li>전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)</li>
	<li>중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)</li>
	<li>후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)</li>
</ul>

<p>가 된다.</p>

### 입력 

 <p>첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.</p>

### 출력 

 <p>첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//https://www.acmicpc.net/problem/1991
//11:14~
//~01:10
//20:10~


typedef struct tree{
    struct tree* left;
    struct tree* right;
    char spell;
}tree;

void init_tree(tree* temp)
{
    temp->left = NULL;
    temp->right = NULL;
    temp->spell = '.';
}


void preorder(tree *current)
{
    printf("%c", current -> spell);
    if(current -> left != NULL)
        preorder(current->left);
    if(current -> right != NULL)
        preorder(current->right);
    return ;
}

void inorder(tree *current)
{
    if(current -> left != NULL)
        inorder(current->left);
    printf("%c", current -> spell);
    if(current -> right != NULL)
        inorder(current->right);
    return ;
}


void postorder(tree *current)
{
    if(current -> left != NULL)
        postorder(current->left);
    if(current -> right != NULL)
        postorder(current->right);
    printf("%c", current -> spell);
    return ;
}




int main(){
int len = 0;
scanf("%d ", &len);

tree** tree_list = (tree**)malloc(sizeof(tree*)*len);//tree포인터 배열

for(int a = 0; a < len; a++)
{
    tree_list[a] = (tree*)malloc(sizeof(tree));
    init_tree(tree_list[a]);
    tree_list[a] -> spell = 'A'+((int)a);//차례대로 A(A+0), B(A+1)....
}

for(int a = 0; a < len; a++)
{
    char current;
    scanf(" %c", &current);
    int current_index = current - 'A';//A, B, C를 0, 1, 2..로 변환, tree_list[index]로 사용
    char left, right = '.';
    scanf(" %c %c", &left, &right);
    int left_index = left - 'A'; 
    int right_index = right-'A';

    if(left != '.')
    {
        tree_list[current_index]->left = tree_list[left_index];
    }
    else
    {
     tree_list[current_index]->left = NULL;   
    }

       if(right != '.')
    {
        tree_list[current_index]->right = tree_list[right_index];
    }
    else
    {
     tree_list[current_index]->right = NULL;   
    }
    
}

preorder(tree_list[0]);
printf("\n");
inorder(tree_list[0]);
printf("\n");
postorder(tree_list[0]);



return 0;
}
```
