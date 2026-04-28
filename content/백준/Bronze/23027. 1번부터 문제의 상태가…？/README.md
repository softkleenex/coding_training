---
title: "[Bronze II] 1번부터 문제의 상태가…? - 23027"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 1번부터 문제의 상태가…? - 23027 

[문제 링크](https://www.acmicpc.net/problem/23027) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

구현, 문자열

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="height: 417px; width: 500px;"></p>

<p>큰일이다. 시험 문제를 본 쿠기는 1번부터 풀 수가 없다. 시험 시간 동안 할 일이 없었던 쿠기는 교수님께 편지를 쓰려고 한다. 작년 시험에서 교수님께 그동안 감사했다는 편지를 전하고 <strong>D+</strong>을 받았던 기억이 있다. 그때 성적이 문제였는지, 편지가 문제였는지 궁금하여 이번에도 1번 문제의 답안 칸에 편지를 작성하려고 한다. 혹시나 하는 마음에 쿠기는 <strong>D+</strong>만은 피하고자 편지를 수정하려고 한다.</p>

<ol>
	<li>편지의 내용 <em>S</em>에 '<code>A</code>'가 있다면 <em>S</em>에 있는 '<code>B</code>', '<code>C</code>', '<code>D</code>', '<code>F</code>'를 모두 '<code>A</code>'로 변경한다.</li>
	<li>'<code>A</code>'가 없고 '<code>B</code>'가 있다면 <em>S</em>에 있는 '<code>C</code>', '<code>D</code>', '<code>F</code>'를 모두 '<code>B</code>'로 변경한다.</li>
	<li>'<code>A</code>'와 '<code>B</code>'가 없고 '<code>C</code>'가 있다면 <em>S</em>에 있는 '<code>D</code>', '<code>F</code>'를 모두 '<code>C</code>'로 변경한다.</li>
	<li>'<code>A</code>', '<code>B</code>'와 '<code>C</code>'가 모두 없다면 <em>S</em>에 있는 모든 문자를 '<code>A</code>'로 변경한다.</li>
</ol>

<p>쿠기를 도와 편지를 수정하는 것을 도와주자.</p>

### 입력 

 <p>편지의 내용 <em>S</em>(1 ≤ <em>S </em>의 길이 ≤ 1,000)가 주어진다. 문자열 <em>S</em>는 알파벳 대문자로 이루어져 있다.</p>

### 출력 

 <p>수정된 편지의 내용을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

#include<string.h>

int check_A(char message[], int len)

{

	for(int a = 0 ;a < len; a++)	{

		if(message[a] == 'A')

		{

			return 1;	

		}

	}

	return 0;	

}

int check_B(char message[], int len)

{

	for(int a = 0 ;a < len; a++)

	{

		if(message[a] == 'B')

		{

			return 1;	

		}

	}

	return 0;	

}

int check_C(char message[], int len)

{

	for(int a = 0 ;a < len; a++)

	{

		if(message[a] == 'C')

		{

			return 1;	

		}

	}

	return 0;	

}

int check(char message[], int len)

{

	if(check_A(message, len) == 1)

		return 1;

	else if(check_B(message, len) == 1)

		return 2;

	else if(check_C(message, len) == 1)

	 return 3;

	 else 

	 	return 4;

	

	

	

	}

int main() {

	char message[1001];

	scanf("%s", message);

	int index = 0;

	char temp = NULL;

	int len = 0;

	

	while (1)

	{

		if(message[len] != '\0')

			len++;

		else

		{

			break;

		}

	}

	

	

	int count = check (message, len);

	switch(count)

	{

		case(1):

	for(int a = 0; a < len; a++)

	{

		message[a] = (message[a] == 'B')||(message[a] == 'C')||(message[a] == 'D')||(message[a] == 'F') ? 'A' : message[a];

		}

		break;	

	case(2):

	for(int a = 0; a < len; a++)

	{

		message[a] = ((message[a] == 'C')||(message[a] == 'D')||(message[a] == 'F')) ? 'B' : message[a];

		}

		break;	

	case(3):

	for(int a = 0; a < len; a++)

	{

		message[a] = (message[a] == 'D')||(message[a] == 'F') ? 'C' : message[a];

		}

		break;	

	case(4):

	for(int a = 0; a < len; a++)

	{

		message[a] = 'A';

		}

		break;		

	}

	

	for(int a = 0; a < len; a++)

	{

		printf("%c", message[a]);

		}

		

		

		

	

	

return 0;

}
```
