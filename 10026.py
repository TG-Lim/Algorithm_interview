# Gold 5
# 1 <= N <= 100 -> O(N^3) okay
import sys
from collections import deque

N = int(sys.stdin.readline())

picture = []
for _ in range(N):
    temp = sys.stdin.readline().strip()
    picture.append(list(temp))

disease = [t[:] for t in picture]
for i in range(N):
    for j in range(N):
        if disease[i][j] == 'R' or disease[i][j] == 'G':
            disease[i][j] = 'S'

deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(n, m, visited, graph):
    if not visited[n][m]:
        queue = deque([(n, m)])
        visited[n][m] = True
        while queue:
            nn, nm = queue.popleft()
            for i in range(4):
                temp_n = nn + deltas[i][0]
                temp_m = nm + deltas[i][1]

                if 0<= temp_n < N and 0 <= temp_m < N and not visited[temp_n][temp_m] and graph[nn][nm] == graph[temp_n][temp_m]:
                    queue.append((temp_n, temp_m))
                    visited[temp_n][temp_m] = True
        return True
    else:
        return False

visited_picture = [[False] * N for _ in range(N)]
cnt = 0 # 하나의 색깔
for i in range(N):
    for j in range(N):
        if bfs(i, j, visited_picture, picture):
            cnt += 1

visited_disease = [[False] * N for _ in range(N)]
cnt_disease = 0
for i in range(N):
    for j in range(N):
        if bfs(i, j, visited_disease, disease):
            cnt_disease += 1

print(cnt, cnt_disease)