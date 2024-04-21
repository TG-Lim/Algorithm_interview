# Silver 1
# 2 <= N <= 100 -> O(N^3)
from collections import deque
N = int(input())
array = []

for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    array.append(temp)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, height, visited):
    queue = deque([])
    queue.append((x, y))
    visited[0][0] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            condition = (0 <= nx < N) and (0 <= ny < N)
            if condition and array[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

answer = 0
for height in range(101):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if array[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited)
                cnt += 1
    answer = max(answer, cnt)
print(answer)