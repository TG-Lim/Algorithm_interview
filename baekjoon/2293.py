import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
array = [int(input()) for _ in range(n)]

dp = [0]*(k+1) # dp[i]: i 원을 만들 수 있는 경우의 수
dp[0] = 1

for a in array:
    for i in range(a, k+1): # 동전들에서 목표까지
        dp[i] += dp[i-a]

print(dp[k])