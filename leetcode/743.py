import heapq
INF = int(1e9)

def dijkstra(start, graphs, distances):
    q = []
    heapq.heappush(q, (0, start)) # 현재 거리, 노드
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist: # 저장된 최단거리가 짧음
            continue
        for g in graphs[now]:
            cost = dist + g[1] # 거쳐서 온 길
            if cost < distances[g[0]]: # 거쳐서 온 게 더 짧음
                distances[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        distances = [INF]*(n+1)

        graphs = [[] for _ in range(n+1)]
        for time in times:
            u, v, t = time[0], time[1], time[2]
            graphs[u].append((v, t)) # u에서 출발, v 도착, t 소요

        dijkstra(k, graphs, distances)

        maximum_delay = 0

        for i in range(1, n+1):
            if distances[i] == INF:
                return -1
            maximum_delay = max(maximum_delay, distances[i])

        return maximum_delay


if __name__ == '__main__':
    cases = [
        ([[2,1,1],[2,3,1],[3,4,1]], 4, 2),
        ([[1,2,1]], 2, 1),
        ([[1,2,1]], 2, 2)
    ]

    for case in cases:
        output = Solution().networkDelayTime(case[0], case[1], case[2])
        print(output)