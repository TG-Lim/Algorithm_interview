# Gold 5
# 배낭채우기, Knapsack -> DP
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
weights = [0]
values = [0]
for _ in range(N):
    w, v = map(int, input().strip().split())
    weights.append(w)
    values.append(v)

dp = [[0]*(K+1) for _ in range(N+1)]
# dp[i][j]: 물건 i 개를 활용하여 무게를 j 만큼 하였을 때 최대 가치

for i in range(1, N+1):
    for j in range(1, K+1):
        if weights[i] > j: # 남아 있는 무게보다 추가될 물건이 무게 더 많음
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]]) # 현재 i 번째 물건 안 넣기 vs 현재 i 번째 물건 넣기

print(dp[N][K])