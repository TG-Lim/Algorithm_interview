# Silver 2
# Graph Search
# 1000개 -> O(N^2) okay

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())

graph = [[False for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i][j] = True
    graph[j][i] = True

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for adjacent_node in range(1, len(graph[v])):
            if graph[v][adjacent_node] and not visited[adjacent_node]:
                queue.append(adjacent_node)
                visited[adjacent_node] = True

cnt = 0
for node in range(1, N+1):
    if not visited[node]:
        bfs(graph, visited, node)
        cnt += 1

print(cnt)