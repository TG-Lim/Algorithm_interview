# Gold 4
# 최단 경로, 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().strip().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w)) # u에서 v 까지 비용이 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용을 우선으로 처리 하기 위해 비용을 첫번째로 두어 힙 자료구조 활용
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 경로가 작으면 패스
            continue
        for i in graph[now]: # i: (목적지, 비용)
            cost = dist + i[1] # 다른 곳 거쳐서 가는 비용
            if cost < distance[i[0]]: # 현재 비용보다 적게 드는경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])