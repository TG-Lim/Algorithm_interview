# Gold 4
import sys
input = sys.stdin.readline

inf = int(1e6)

n, m, r = map(int, input().strip().split())
items = [0]
items += list(map(int, input().strip().split()))

graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().strip().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

best_item = 0

for start_point in range(1, n+1): # 1번 부터 n 번까지 시작점
    temp = 0
    for node in range(1, n+1):
        if graph[start_point][node] <= m:
            temp += items[node]
    
    best_item = max(best_item, temp)

print(best_item)