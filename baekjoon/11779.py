# Gold 3
import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [{} for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

departure, arrival = map(int, input().strip().split())

def dijkstra(departure):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[departure] = 0
    path = [-1] * (n + 1)
    pq = [(0, departure)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > distance[current_node]:
            continue

        for adj_node, adj_cost in graph[current_node].items():
            cost = current_cost + adj_cost
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                path[adj_node] = current_node
                heapq.heappush(pq, (cost, adj_node))

    return distance, path

distance, path = dijkstra(departure, arrival)

best_cost = distance[arrival]
best_path = []
node = arrival
while node != -1:
    best_path.append(node)
    node = path[node]
best_path.reverse()
print(best_cost)
print(len(best_path))
sys.stdout.write(' '.join(map(str, best_path)))