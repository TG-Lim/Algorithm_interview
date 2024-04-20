# Gold 3
# 1<= N, M <= 1000 -> O(N^2)
import sys
from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0]*2 for _ in range(M)]for _ in range(N)]
visited[0][0][0] = 1

def bfs():
    queue = deque([])
    queue.append((0,0,0))

    while queue:
        x, y, w = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 and w == 0: # 벽이고, 아직 벽을 뿌순 적 없음
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            if graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 벽이 아니고, 방문 안한 경우
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append((nx, ny, w))

    return -1

print(bfs())