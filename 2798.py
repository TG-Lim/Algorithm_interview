import sys
from itertools import combinations

N, M = map(int, input().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

card_combination = list(combinations(cards, 3))


best_case = 0

for case in card_combination:
    case_sum = sum(case)

    if case_sum <= M:
        best_case = max(best_case, case_sum)

print(best_case)