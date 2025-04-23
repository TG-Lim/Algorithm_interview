import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
degree = [0] * (V+1)

# 1) 그래프 읽기 및 차수(degree) 계산
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    degree[u] += 1
    degree[v] += 1

# 2) (연결성 검사) 간선이 있는 첫 정점 찾기
start = 1
while start <= V and degree[start] == 0:
    start += 1

# 모든 정점 차수 0  → 간선이 하나도 없는 그래프 → trivially YES
if start > V:
    print("YES")
    sys.exit(0)

# BFS/DFS 로 연결성 확인: degree>0인 정점만 세야 함
visited = [False] * (V+1)
queue = deque([start])
visited[start] = True
count_conn = 1  # 연결된 degree>0 정점 수

while queue:
    x = queue.popleft()
    for y in adj[x]:
        if not visited[y]:
            visited[y] = True
            # 실제 간선이 있는 정점이면 카운트
            count_conn += 1
            queue.append(y)

total_nonzero = sum(1 for i in range(1, V+1) if degree[i] > 0)
if count_conn != total_nonzero:
    print("NO")  # 연결성 실패
    sys.exit(0)

# 3) 홀수 차수 정점 개수 검사
odd = sum(1 for i in range(1, V+1) if degree[i] % 2 == 1)
# 회로(0개)거나 경로(2개) 가능
if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")
