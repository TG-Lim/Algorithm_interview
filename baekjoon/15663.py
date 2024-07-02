# Silver 2
from itertools import permutations
N, M = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

permutation = permutations(range(N), M)

temp = set()

for comb in permutation:
    temp2 = []
    for c in comb:
        temp2.append(array[c])
    temp2.sort()
    if temp2 not in temp:
        temp.add(temp2)

print(temp)