# Silver 2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

adjacent_list = [
    [] for _ in range(N+1)
]
parent_node = [0]*(N+1)

visited = [False]*(N+1)

for _ in range(N-1):
    a, b = map(int, input().strip().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)

queue = deque([])
# root node
queue.append(1)
visited[1] = True

while queue:
    v = queue.popleft()
    adjacent_nodes = adjacent_list[v]

    for adjacent_node in adjacent_nodes:
        if not visited[adjacent_node]:
            visited[adjacent_node] = True
            parent_node[adjacent_node] = v
            queue.append(adjacent_node)

sys.stdout.write('\n'.join(str(n) for n in parent_node[2:]))