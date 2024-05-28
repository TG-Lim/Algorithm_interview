# Silver 2
# DFS

import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def dfs(x, y, visited):
    if not visited[x][y] and array[x][y] == 1:
        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            condition = (0 <= nx < h) and (0 <= ny < w)
            if condition and array[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, visited)
        return True
    else:
        return False

result = []
while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    visited = [[False]*w for _ in range(h)]
    array = []
    for _ in range(h):
        array.append(list(map(int, input().strip().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, visited):
                cnt += 1
    result.append(cnt)
print('\n'.join(str(r) for r in result))