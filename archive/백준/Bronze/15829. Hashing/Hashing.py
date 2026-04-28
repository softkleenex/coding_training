#pylint:disable=W1309
def arr_sum(arr1):
	a = 0
	for index, value in enumerate(arr1):
		a += ((int(ord(value))-96)*(31**index))
	return a%1234567891
		
L = int(input())

while True:
		string = (input())
		if len(string) == L:
			break

print(arr_sum(string))