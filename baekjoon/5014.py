# Silver 1
from collections import deque
F, S, G, U, D = map(int, input().split())

visited = [False]*(F+1)
result = [0]*(F+1)


if S == G:
    print(0)
    exit()

def bfs(number, visited):
    queue = deque([number])
    visited[number] = True
    while queue:
        v = queue.popleft()
        if v+U <= F and not visited[v+U]:
            queue.append(v+U)
            visited[v+U] = True
            result[v+U] = result[v]+1
        if v-D >= 1 and not visited[v-D]:
            queue.append(v-D)
            visited[v-D] = True
            result[v-D] = result[v]+1

bfs(S, visited)
if result[G] == 0:
    print("use the stairs")
else:
    print(result[G])