import sys
N = int(sys.stdin.readline().strip())
list1= [0] * 10001

for _ in range(N):
	a = int(sys.stdin.readline().strip())
	list1[a] += 1
	
for index, value in enumerate(list1):
	if value != 0:
		for i in range(value):
			sys.stdout.write(f"{index}\n")