# Silver 1
import sys
from itertools import combinations

T = int(input())

def distance(mbti_array):
    combs = combinations(mbti_array, 3)
    min_distance = int(1e6)
    for comb in combs:
        temp = 0
        for i in range(4):
            if comb[0][i] != comb[1][i]:
                temp += 1
            if comb[1][i] != comb[2][i]:
                temp += 1
            if comb[0][i] != comb[2][i]:
                temp += 1
        if temp <= min_distance:
            min_distance = temp
    return min_distance

result = []
for _ in range(T):
    t = int(input())
    mbti_array = list(sys.stdin.readline().rstrip().split())
    if t > 32:
        result.append('0')
    else:
        result.append(str(distance(mbti_array)))
print('\n'.join(result))
