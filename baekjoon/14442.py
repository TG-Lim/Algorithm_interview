import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().strip().split())

building = [list(input().strip()) for _ in range(N)]

# visited[r][c][k] : r,c 위치에 벽을 k번 부수고 방문했는지 여부
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0, 1, 0))  # r, c, 이동거리, 부순 벽 수
visited[0][0][0] = True

while queue:
    r, c, dist, broken = queue.popleft()

    if r == N - 1 and c == M - 1:
        print(dist)
        exit()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            # 다음 칸이 벽이 아닌 경우
            if building[nr][nc] == '0' and not visited[nr][nc][broken]:
                visited[nr][nc][broken] = True
                queue.append((nr, nc, dist + 1, broken))
            # 벽이면서 아직 부술 수 있는 경우
            elif building[nr][nc] == '1' and broken < K and not visited[nr][nc][broken + 1]:
                visited[nr][nc][broken + 1] = True
                queue.append((nr, nc, dist + 1, broken + 1))

print(-1)