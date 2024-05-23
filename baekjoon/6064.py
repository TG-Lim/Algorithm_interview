# Silver 1
# 1 <= M, N <= 40000

import sys
from math import lcm
input = sys.stdin.readline
T = int(input())


def solution(M, N, x, y):
    if M == x and N == y:
        return lcm(M, N)
    answer = False
    year = None
    end = lcm(M, N)
    for i in range(N+1):
        number = M*i + x
        if (number-y) % N == 0 and number < end:
            answer = True
            year = number
    if answer:
        return year
    else:
        return -1
    

result = []
for _ in range(T):
    M, N, x, y = map(int, input().strip().split())
    answer = solution(M, N, x, y)
    result.append(answer)
print('\n'.join(str(r) for r in result))
