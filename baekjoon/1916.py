# Gold 5
# 최단 경로
import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

start, end = map(int, input().strip().split())

distance = [inf]*(N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 거쳐간 거리가 현재 비용보다 쌈
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])