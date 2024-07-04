# Gold 4

N = int(input())
dna = input().strip()

dp = [[float('inf')] * N for _ in range(2)]

if dna[0] == 'A':
    dp[0][0] = 0
    dp[1][0] = 1
else:
    dp[0][0] = 1
    dp[1][0] = 0

for i in range(1, N):
    if dna[i] == 'A':
        dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + 1)
        dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 1)
    else:
        dp[0][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 1)
        dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1])

print(dp[0][N - 1])