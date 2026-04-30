import collections
from collections import Counter

n, k = map(int, input().split())
a = Counter(list(map(int, input().split()))).items()

a = sorted(list(x[0] * x[1] for x in a))
# print(a)

a = sum(a[0 : len(a) - k]) if len(a) - k > 0 else 0

print(a)

