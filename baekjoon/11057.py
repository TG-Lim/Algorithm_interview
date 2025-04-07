import sys
input = sys.stdin.readline

N = int(input())

if N == 1: # 0도 포함
    print(10)
    exit()

# dp[i][j]: 문자열 길이가 i 이고 제일 끝 자리 수가 j 일때 개수

dp = [[1]*10 for _ in range(N+1)]
for n in range(2, N+1):
    for i in range(1, 10):
        dp[n][i] = sum(dp[n-1][1:i+1])

print(dp)