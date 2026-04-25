def check(m, arr):
	data = 0
	for i in arr:
		data = data + i
		
	if data > m:
		return 0
	else:
		#print(data)
		return data
			
def combination(m, arr):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    maxsum = [0]

    # 2.
    def generate(chosen):
        if len(chosen) == 3:
            maxsum[0] = max(maxsum[0], check(m, chosen))
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
    return maxsum[0]




#n과 M 을  A B형식으로 입력 받기

N, M = [int(x) for x in input().split()]


arr1 =  list(map(int, input().split()))


#print(N, M, arr1)


print(combination(M, arr1))


