import sys
input = sys.stdin.readline
cnt = 0
while True:
    N = int(input())
    if N == 0:
        exit()
    cnt += 1
    array = [list(map(int, input().strip().split())) for _ in range(N)]

    dp = [[0, 0, 0] for _ in range(N)] # dp[i][j] : i행 j열로 가는데 최소 비용

    dp[0][0] = int(1e9) # 출발 안함
    dp[0][1] = array[0][1]
    dp[0][2] = array[0][1] + array[0][2]

    for i in range(1, N):
        dp[i][0] = array[i][0] + min(dp[i-1][0], dp[i-1][1])
        dp[i][1] = array[i][1] + min(min(dp[i-1]), dp[i][0])
        dp[i][2] = array[i][2] + min(dp[i-1][1], dp[i-1][2], dp[i][1])
    
    print(f'{cnt}. {dp[-1][1]}')