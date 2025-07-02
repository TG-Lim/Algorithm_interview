import sys

N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    # 최악의 경우: 모두 1^2만 쓴 경우 (i개)
    dp[i] = i
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[N])