import sys
import heapq
INF = int(1e12)

input = sys.stdin.readline

cases = int(input())
answers = []
def dijkstra(graph, distance, c):
    distance[c] = 0
    q = [] # Priority Queue

    heapq.heappush(q, (0, c)) # 시간, 컴퓨터

    while q:
        time, computer = heapq.heappop(q)
        if distance[computer] < time:
            continue
        for adj_com, diff_time in graph[computer]:
            cost = distance[computer] + diff_time
            if cost < distance[adj_com]:
                distance[adj_com] = cost
                heapq.heappush(q, (cost, adj_com)) # 시간, 컴퓨터

for _ in range(cases):
    n, d, c = map(int, input().strip().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().strip().split())
        graph[b].append((a, s)) # 컴퓨터, 시간

    distance = [INF]*(n+1)
    dijkstra(graph, distance, c)

    answer_cnt = 0
    answer_time = 0

    for i in range(1, n+1):
        if distance[i] < INF:
            answer_cnt += 1
            answer_time = max(answer_time, distance[i])

    answers.append((answer_cnt, answer_time))

for answer in answers:
    print(answer[0], answer[1])