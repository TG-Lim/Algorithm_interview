# Gold 4
# 3 <= N, M <= 8 -> Time Complexity almost No limit

import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(temp)

empty_rooms = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 빈 칸 목록 확보
            empty_rooms.append((i,j))

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(n, m, visited, temp_graph):
    queue = deque([(n, m)])
    visited[n][m] = True

    while queue:
        nn, nm = queue.popleft()
        for i in range(4):
            temp_n = nn + deltas[i][0]
            temp_m = nm + deltas[i][1]

            if 0<= temp_n < N and 0<= temp_m < M and not visited[temp_n][temp_m] and temp_graph[temp_n][temp_m] != 1:
                queue.append((temp_n, temp_m))
                visited[temp_n][temp_m] = True

                if temp_graph[temp_n][temp_m] == 0:
                    temp_graph[temp_n][temp_m] = 2 # 새로운 곳 병 전염

def zero_count(temp_graph):
    cnt = 0
    for n in range(N):
        for m in range(M):
            if temp_graph[n][m] == 0:
                cnt += 1

    return cnt

safe_space = 0
for i in combinations(empty_rooms, 3): # O(N^3)
    temp_graph = [row[:] for row in graph]
    visited = [[False]*M for _ in range(N)]

    for j in range(3):
        temp_graph[i[j][0]][i[j][1]] = 1

    for n in range(N):
        for m in range(M):
            if not visited[n][m] and temp_graph[n][m] == 2:
                bfs(n, m, visited, temp_graph)

    temp = zero_count(temp_graph)

    if temp > safe_space:
        safe_space = temp


print(safe_space)