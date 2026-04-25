def find1(arr):
	for i in range (max(arr), 0, -1):
		if(arr[0] % i == 0 and arr[1] % i == 0):
			return i
	return False
		
def find2(arr):
	num1 = min(arr)
	while True:
		if(num1 % max(arr)) == 0 and num1 >= max(arr):
			return num1
		elif(num1 >= min(arr) * max(arr)): 
				return min(arr)*max(arr)
		else:
			num1 = num1 + min(arr)
		#	print("!", num1)
		

arr_numbers = list(map(int, input().split()))


print(find1(arr_numbers))
print(find2(arr_numbers))