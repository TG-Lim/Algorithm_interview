# Gold 5
import sys
input = sys.stdin.readline

N = int(input())
array = [[0] * (N+1) for _ in range(N+1)]
prefix_sum = [[0] * (N+1) for _ in range(N+1)]

answer = None

# 입력 받기 및 누적 합 계산
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        array[i][j] = row[j-1]
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + array[i][j]

answer = float('-inf')

# 모든 가능한 정사각형에 대해 합 계산
for k in range(1, N+1):
    for i in range(k, N+1):
        for j in range(k, N+1):
            sum_value = prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + prefix_sum[i-k][j-k]
            answer = max(answer, sum_value)

print(answer)