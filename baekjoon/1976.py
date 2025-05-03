import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graphs = {i: [] for i in range(1, N+1)}

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j, t in enumerate(temp):
        if t == 1:
            graphs[i+1].append(j+1)

paths = list(map(int, input().strip().split()))

def check_available(start, end):
    visited = [False]*(N+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for adj_node in graphs[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                queue.append(adj_node)
    
    if not visited[end]: # 못 감
        return False
    else:
        return True

available = True
for i in range(M-1):
    start, end = paths[i], paths[i+1]
    if not check_available(start, end):
        print("NO")
        exit()

print('YES')
exit()