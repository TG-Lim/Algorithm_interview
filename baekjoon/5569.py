import sys
input = sys.stdin.readline
mod = 100000

def solution():
    w, h = map(int, input().split())
    
    # dp[r][c][direction][changed]
    # direction: 0(오른쪽), 1(위)
    # changed: 0(직진), 1(방향전환)
    dp = [[[[0] * 2 for _ in range(2)] for _ in range(w)] for _ in range(h)]

    # 초기값 설정: (0,0)에서 출발
    # (0,1)로 가는 경우와 (1,0)으로 가는 경우는 각각 1가지
    if w > 1:
        dp[0][1][0][0] = 1 # (0,0)에서 오른쪽으로 이동
    if h > 1:
        dp[1][0][1][0] = 1 # (0,0)에서 위쪽으로 이동

    for r in range(h):
        for c in range(w):
            # 현재 (r,c)에 대해, 다음 위치 (r, c+1) 또는 (r+1, c)로 가는 경로의 수를 계산
            
            # 1. 오른쪽으로 이동하여 (r, c+1)에 도달하는 경우
            if c + 1 < w:
                # 1-1. 직진 (오른쪽 -> 오른쪽)
                # (r,c)에 오른쪽으로 직진해서 왔거나, 방향을 바꿔서 왔어도 다음엔 직진 가능
                dp[r][c+1][0][0] = (dp[r][c+1][0][0] + dp[r][c][0][0] + dp[r][c][0][1]) % mod
                
                # 1-2. 방향 전환 (위 -> 오른쪽)
                # (r,c)에 직진으로 도착했을 때만 방향 전환 가능
                dp[r][c+1][0][1] = (dp[r][c+1][0][1] + dp[r][c][1][0]) % mod

            # 2. 위쪽으로 이동하여 (r+1, c)에 도달하는 경우
            if r + 1 < h:
                # 2-1. 직진 (위 -> 위)
                dp[r+1][c][1][0] = (dp[r+1][c][1][0] + dp[r][c][1][0] + dp[r][c][1][1]) % mod
                
                # 2-2. 방향 전환 (오른쪽 -> 위)
                dp[r+1][c][1][1] = (dp[r+1][c][1][1] + dp[r][c][0][0]) % mod
                
    # 최종 결과: (h-1, w-1)에 모든 방향, 모든 상태로 도착한 경우의 합
    answer = sum(dp[h-1][w-1][0]) + sum(dp[h-1][w-1][1])
    print(answer % mod)

solution()