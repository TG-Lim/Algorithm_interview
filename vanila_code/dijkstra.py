import sys
import heapq

input = sys.stdin.readline
INF = int(1e6)

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    d, a, c = map(int, input().strip().split())
    graph[d].append((a, c))

distances = [INF]*(N+1)

start = 1 # 1번 노드 출발

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue

        for adj in graph[now]:
            a, c = adj[0], adj[1]
            if c + dist < distances[a]:
                distances[a] = c + dist
                heapq.heappush(q, (c+dist, a))


dijkstra(start)

for i in range(1, N+1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])


"""
입력용

6 9
1 2 12
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
"""