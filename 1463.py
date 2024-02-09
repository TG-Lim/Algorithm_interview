# BOJ Silver 3
# Dynamic Programming

import sys
n = int(sys.stdin.readline())

result = [0 for _ in range(int(1e6)+1)]
result[2] = 1
result[3] = 1

for i in range(4, int(1e6)+1):
    if i % 2 == 0: # 2로 나누어지는 경우
        if i % 3 == 0: # 2, 3 둘다 나누어 지는 경우
            result[i] = 1 + min(result[i//2], result[i//3], result[i-1])
        else:
            result[i] = 1 + min(result[i//2], result[i-1])
    elif i % 3 == 0: # 3으로 나누어 지는 경우
        result[i] = 1 + min(result[i//3], result[i-1])
    else: # 둘다 아닌 경우
        result[i] = 1+ result[i-1]

print(result[n])