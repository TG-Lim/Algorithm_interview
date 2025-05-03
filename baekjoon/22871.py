import sys
input = sys.stdin.readline


N = int(input())
array = list(map(int, input().strip().split()))
inf = int(1e10)
dp = [0] + [inf]*(N-1)

for i in range(1, N):
    for j in range(0, i):
        power = max((i-j)*(1+abs(array[i]-array[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[N-1])