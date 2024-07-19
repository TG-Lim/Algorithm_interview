# Silver 1
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().strip().split())))

visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    picture = 1
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            condition = (0<= nx < n) and (0 <= ny < m)
            if condition and not visited[nx][ny] and array[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                picture += 1
    
    return picture
cnt = 0
best_picture = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 1:
            cnt += 1
            picture = bfs(i, j)
            best_picture = max(best_picture, picture)
print(cnt)
print(best_picture)