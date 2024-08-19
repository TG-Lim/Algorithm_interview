# Silver 1
import sys
from itertools import combinations, permutations

input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

combs = combinations(range(N), N//2) # 20C10 = 184756

best = int(1e9)

for comb in combs:
    team1 = set(comb)
    team2 = set(range(N)) - team1
    
    permutation1 = permutations(team1, 2)
    score1 = 0
    for permu in permutation1:
        score1 += array[permu[0]][permu[1]]
    
    permutation2 = permutations(team2, 2)
    score2 = 0
    for permu in permutation2:
        score2 += array[permu[0]][permu[1]]
    
    temp = abs(score1-score2)

    best = min(best, temp)

print(best)