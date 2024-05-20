# Silver 1

big_number = int(1e9)
N = int(input())
dp = [[0]*10 for _ in range(N+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 9: # 끝 자리가 9는 무조건 8에서 추가
            dp[i][j] = dp[i-1][j-1]
        elif j == 0: # 끝 자리가 0은 무조건 1에서 옴
            dp[i][j] = dp[i-1][j+1]
        else: # 나머지는 2 방향에서 옴
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(int(sum(dp[N]) % big_number))