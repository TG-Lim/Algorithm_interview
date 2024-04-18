# Silver 1
# 2<= n <= 1000, 2<= m <= 1000
import sys
from collections import deque

n, m = map(int, input().split())
array = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    array.append(temp)
visited = [[False]*m for _ in range(n)]
start_x = 0
start_y = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            start_x, start_y = i, j
            break
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
array[start_x][start_y] = 0
visited[start_x][start_y] = True
queue = deque([(start_x, start_y)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visited[nx][ny] and array[nx][ny] == 1:
            visited[nx][ny] = True
            array[nx][ny] = array[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] != 0: # 원래 갈 수 있었으나 못감
            array[i][j] = -1

for i in range(n):
    print(' '.join(str(a) for a in array[i]))