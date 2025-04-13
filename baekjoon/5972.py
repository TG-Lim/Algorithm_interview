import heapq
import sys
inf = int(1e10)
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = [[] for _ in range(N+1)]
temp = {}
for _ in range(M):
    a, b, c = map(int, input().strip().split()) # 출발, 도착, 비용 (양방향)
    if (a, b) not in temp:
        temp[(a, b)] = c
    else:
        temp[(a, b)] = min(temp[(a, b)], c)

for key, value in temp.items():
    array[key[0]].append((key[1], value))
    array[key[1]].append((key[0], value))

if N == 1:
    print(0)
    exit()

distance = [inf]*(N+1)
distance[1] = 0 # 현서 초기 위치
q = [(0, 1)] # 거리, 노드

while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
        continue
    for adj_node, cost in array[node]:
        new_cost = dist + cost
        if new_cost < distance[adj_node]:
            distance[adj_node] = new_cost
            heapq.heappush(q, (new_cost, adj_node))

print(distance[N])