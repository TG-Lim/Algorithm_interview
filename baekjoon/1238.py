# Gold 3
# 개선 다익스트라 알고리즘
import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

N, M, X = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
time = [inf]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue

        for i in graph[now]:
            cost = t + i[1]
            if cost <= time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

go = []
back = []

for i in range(1, N+1):
    if i != X:
        time = [inf]*(N+1)
        dijkstra(i)
        go.append((i, time[X]))

time = [inf]*(N+1)
dijkstra(X)
for i in range(1, N+1):
    if i != X:
        back.append((i, time[i]))

maximum = 0
for i in range(len(go)):
    maximum = max(maximum, go[i][1]+back[i][1])

print(maximum)