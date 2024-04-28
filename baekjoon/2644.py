# Silver 2
inf = int(1e9)
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [inf]*(n+1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def get_smallest_node():
    min_value = inf
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j] = 1

    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        if graph[now]:
            for j in graph[now]:
                cost = distance[now] + 1
                if cost <= distance[j]:
                    distance[j] = cost
        else:
            continue

start = a
dijkstra(start)
if distance[b] != inf:
    print(distance[b])
else:
    print(-1)