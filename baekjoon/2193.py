N = int(input())
dp = [[0, 0] for _ in range(N+1)] # dp[i][j]: 자리수가 i 이고, 끝이 j 로 끝나는 이친수 개수. (j= 0, 1)

dp[1][0] = 0 # 없음
dp[1][1] = 1 # 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] # 0으로 끝나는 거는 앞자리에 1, 0 둘다 올 수 있음
    dp[i][1] = dp[i-1][0] # 1로 끝나는 거는 무조건 앞에 0으로 끝날때만 올 수 있음

print(sum(dp[-1]))