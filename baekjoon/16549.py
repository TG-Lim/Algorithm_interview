# Silver 3
from itertools import permutations

N, M = map(int, input().split())
array = [i for i in range(1, N+1)]
permutation = permutations(array, M)
for p in permutation:
    temp = list(p)
    print(' '.join(str(t) for t in temp))