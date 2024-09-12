# Silver 2
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

answer = 0

for c in range(1, N+1):
    combination = combinations(array, c)
    for comb in combination:
        if sum(comb) == S:
            answer += 1

print(answer)