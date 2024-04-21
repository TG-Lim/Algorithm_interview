# Silver 1
# 2 <= N <= 100 -> O(N^3)
import sys
sys.setrecursionlimit(100000)
N = int(input())
array = []

for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    array.append(temp)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(height, x, y, visited):
    if not visited[x][y] and array[x][y] > height:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            condition = (0 <= nx < N) and (0 <= ny < N)
            if condition:
                dfs(height, nx, ny, visited)
        return True
    return False

answer = 0
for height in range(101):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dfs(height, i, j, visited):
                cnt += 1
    answer = max(answer, cnt)
print(answer)