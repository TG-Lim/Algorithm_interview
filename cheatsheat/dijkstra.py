import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().strip().split())
start = int(input())

inf = int(1e9)

graph = [[] for i in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c)) # 도착지, 거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 힙 자료구조가 빌 때까지
        dist, now = heapq.heappop(q) # 거리, 노드

        if distance[now] < dist: # 이미 더 업데이트 된 경우
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 도착지에 있는 거리 보다 cost가 작은 경우 업데이트
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])


"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""