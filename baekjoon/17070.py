N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

# DP 테이블 초기화
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 초기 상태: 가로로 놓여진 상태

for i in range(N):
    for j in range(1, N):
        if array[i][j] == 1:
            continue
        # 가로로 놓여진 상태에서의 경로 수 업데이트
        if j > 0 and array[i][j-1] == 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        # 세로로 놓여진 상태에서의 경로 수 업데이트
        if i > 0 and array[i-1][j] == 0:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        # 대각선으로 놓여진 상태에서의 경로 수 업데이트
        if i > 0 and j > 0 and array[i-1][j] == 0 and array[i][j-1] == 0 and array[i-1][j-1] == 0:
            dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

# 모든 경로의 합을 계산
result = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(result)