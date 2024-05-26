# Gold 3
# 1 <= M, N <= 500
# BFS
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
array = []
M, N = map(int, input().strip().split())

for _ in range(M):
    array.append(list(map(int, input().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1]*N for _ in range(M)]

def condition(x, y, now):
    return (0 <= x < M) and (0 <= y < N) and (array[x][y] < now)

def dfs(x, y):
    if (x == M-1) and (y == N-1):
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if condition(nx, ny, array[x][y]):
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))