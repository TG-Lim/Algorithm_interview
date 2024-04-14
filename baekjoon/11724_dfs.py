# Silver 2
# Graph Search
# 1000개 -> O(N^2) okay

import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().strip().split())

graph = [[False for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i][j] = True
    graph[j][i] = True

cnt = 0

def dfs(node, visited, graph):
    # 방문처리
    if not visited[node]:
        visited[node] = True
        for v in range(len(graph[node])):
            if not visited[v] and graph[node][v]: # 연결되어 있고, 아직 방문 안한 경우
                dfs(v, visited, graph)
        return True
    
    return False

for i in range(1,N+1):
    if dfs(i, visited, graph):
        cnt += 1

print(cnt)