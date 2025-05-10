import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().strip().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w)) # 도착지, 비용

inf = int(1e9)
distance = [inf]*(V+1)
distance[K] = 0
q = [(0, K)] # 거리, 정점

while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for adj_node, cost in graph[node]:
        if dist + cost < distance[adj_node]:
            distance[adj_node] = dist+cost
            heapq.heappush(q, (dist+cost, adj_node))

for dist in distance[1:]:
    if dist == inf:
        print('INF')
    else:
        print(dist)