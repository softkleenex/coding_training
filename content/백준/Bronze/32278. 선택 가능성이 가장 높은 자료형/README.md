---
title: "[Bronze IV] 선택 가능성이 가장 높은 자료형 - 32278"
tags: ["백준", "Bronze IV"]
---

# [Bronze IV] 선택 가능성이 가장 높은 자료형 - 32278 

[문제 링크](https://www.acmicpc.net/problem/32278) 

### 성능 요약

메모리: 34536 KB, 시간: 40 ms

### 분류

구현

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>선린이는 효율적으로 코딩하는 걸 좋아해서 아래와 같은 방식으로 자료형을 선택한다고 한다. 선린이가 선택할 자료형을 알아내자!</p>

<p><strong>선린이가 자료형을 선택하는 기준은 다음과 같다.</strong></p>

<ul>
	<li>정확하게 표현할 수 있으면서, 메모리를 적게 차지하는 자료형을 선택한다.</li>
	<li>선택할 수 있는 자료형은 <span style="color:#e74c3c;"><code>short</code></span>, <span style="color:#e74c3c;"><code>int</code></span>, <span style="color:#e74c3c;"><code>long long</code></span> 중 하나이다.</li>
</ul>

<table class="table table-bordered td-center td-middle table-center-60">
	<tbody>
		<tr>
			<td>자료형</td>
			<td>최솟값</td>
			<td>최댓값</td>
		</tr>
		<tr>
			<td><span style="color:#e74c3c;"><code>short</code></span></td>
			<td>
			<p>$-2^{15}$</p>

			<p>$-32,768$</p>
			</td>
			<td>
			<p>$2^{15}-1$</p>

			<p>$32,767$</p>
			</td>
		</tr>
		<tr>
			<td><span style="color:#e74c3c;"><code>int</code></span></td>
			<td>
			<p>$-2^{31}$</p>

			<p>$-2,147,483,648$</p>
			</td>
			<td>
			<p>$2^{31}-1$</p>

			<p>$2,147,483,647$</p>
			</td>
		</tr>
		<tr>
			<td><span style="color:#e74c3c;"><code>long long</code></span></td>
			<td>
			<p>$-2^{63}$</p>

			<p>$-9,223,372,036,854,775,808$</p>
			</td>
			<td>
			<p>$2^{63}-1$</p>

			<p>$9,223,372,036,854,775,807$</p>
			</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>정수 $N$이 주어진다.</p>

### 출력 

 <p>선린이가 선택할 자료형을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 선린이는 효율적으로 코딩하는 걸 좋아해서 아래와 같은 방식으로 자료형을 선택한다고 한다. 선린이가 선택할 자료형을 알아내자!

# 선린이가 자료형을 선택하는 기준은 다음과 같다.

# 정확하게 표현할 수 있으면서, 메모리를 적게 차지하는 자료형을 선택한다.
# 선택할 수 있는 자료형은 short, int, long long 중 하나이다.
# 자료형	최솟값	최댓값
# short	
#  
# $-2^{15}$ 

#  
# $-32,768$ 

#  
# $2^{15}-1$ 

#  
# $32,767$ 

# int	
#  
# $-2^{31}$ 

#  
# $-2,147,483,648$ 

#  
# $2^{31}-1$ 

#  
# $2,147,483,647$ 

# long long	
#  
# $-2^{63}$ 

#  
# $-9,223,372,036,854,775,808$ 

#  
# $2^{63}-1$ 

#  
# $9,223,372,036,854,775,807$ 

# 입력
# 정수 
# $N$이 주어진다.

# 출력
# 선린이가 선택할 자료형을 출력한다.

# 제한
#  
# $-2^{63}\leq N\leq 2^{63}-1$ 
# 다른 표현으로, 
# $N$은 C++의 long long 범위 안에 들어온다.


import math

n = int(input())

t_short1 = -32768
t_short2 = 32767

t_int1= -math.pow(2, 31)
t_int2= -t_int1 - 1

t_longlong1 = -math.pow(2, 63)
t_longlong2 =  -t_longlong1 -1



if(t_short1 <= n <= t_short2):
    print('short')
elif(t_int1 <= n <= t_int2):
    print('int')
else:
    print('long long')
```
