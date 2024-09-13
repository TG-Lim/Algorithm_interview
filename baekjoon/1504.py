# Gold 4
import sys
import heapq

input = sys.stdin.readline
inf = float('inf')

def dijkstra(departure, arrival):
    if departure == arrival:
        return 0
    distance = [inf]*(N+1)
    q = []
    heapq.heappush(q, (0, departure)) # 거리, 지점
    distance[departure] = 0 # 시작점 거리를 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 이미 최단거리
            continue

        for i in range(1, N+1):
            cost = dist + graph[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance[arrival]

if __name__ == '__main__':
    N, E = map(int, input().strip().split())
    graph = [[inf]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        graph[i][i] = 0

    for _ in range(E):
        a, b, c = map(int, input().strip().split())
        graph[a][b] = c
        graph[b][a] = c

    v1, v2 = map(int, input().strip().split())

    case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
    case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

    if case1 != inf or case2 != inf:
        print(min(case1, case2))
    else:
        print(-1)