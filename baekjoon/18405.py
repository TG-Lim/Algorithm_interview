# GOld 5
# 1 <= N <= 200 -> O(N^3)
from collections import deque
N, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def check_all_visited(visited):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt += 1
    if cnt == N*N:
        return True
    else:
        return False
def bfs(i, j, visited):
    virus = 1001
    visited[i][j] = True
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        condition = (0 <= nx < N) and (0 <= ny < N)
        if condition and array[nx][ny] != 0:
            if array[nx][ny] <= virus:
                virus = array[nx][ny]
    if virus != 1001:
        return virus
    else:
        return 0

for s in range(S):
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if array[i][j] != 0:
                visited[i][j] = True
    if check_all_visited(visited): # 모두 방문한 경우 탈출
        break
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                virus = bfs(i, j, visited)
                queue.append((virus, i, j))
    while queue:
        virus, x, y = queue.popleft()
        array[x][y] = virus
print(array[X-1][Y-1])