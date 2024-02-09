import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

visited = [False for _ in range(n+1)]
adjancent_matrix = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adjancent_matrix[a][b] = True
    adjancent_matrix[b][a] = True

length = 0
def dfs(v, visited):
    visited[v] = True
    length = 1
    for adjacent_node in range(1, len(adjancent_matrix[v])):
        if adjancent_matrix[v][adjacent_node] and not visited[adjacent_node]: # 연결되어있고, 아직 방문 X
            length += dfs(adjacent_node,visited)
    return length

result = dfs(1, visited)
print(result-1) # 1번 컴퓨터 제외