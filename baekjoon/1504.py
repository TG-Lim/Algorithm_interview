# Gold 4
import sys

input = sys.stdin.readline
inf = int(1e6)
N, E = map(int, input().strip().split())
graph = [[inf]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().strip().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().strip().split())

print(graph)