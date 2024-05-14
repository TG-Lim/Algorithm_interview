# Silver 3
from itertools import combinations

N, M = map(int, input().split())
array = [i for i in range(1, N+1)]
combination = combinations(array, M)
for c in combination:
    temp = list(c)
    temp.sort()
    print(' '.join(str(t) for t in temp))