# Gold5
# Graph Search
# 0< N, M, H <= 100 -> O(N^3) okay

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split()) # M : 가로, N : 세로, H : 높이

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

tomatoes = [[] for _ in range(H)]
ripens = []
for i in range(N*H):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    layer = int(i//N)
    tomatoes[layer].append(temp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                ripens.append((i, j, k))


delta = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
queue = deque([])

for location in ripens:
    queue.append(location)
    visited[location[0]][location[1]][location[2]] = True # 미리 익은 것들 방문 처리

day = 0

while queue:
    v = queue.popleft()
    for i in range(6):
        new_h, new_n, new_m = v[0]+delta[i][0], v[1] + delta[i][1], v[2]+delta[i][2]
        range_in = 0 <= new_h < H and 0 <= new_n < N and 0 <= new_m < M
        if not range_in:
            continue
        if not visited[new_h][new_n][new_m] and tomatoes[new_h][new_n][new_m] == 0:
            queue.append((new_h, new_n, new_m))
            visited[new_h][new_n][new_m] = True
            tomatoes[new_h][new_n][new_m] = tomatoes[v[0]][v[1]][v[2]] + 1

day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0: # 안익은 경우
                print(-1)
                exit(0)
        day = max(day, max(tomatoes[i][j]))

print(day-1)