# Gold 3
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

viruses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            viruses.append((i, j))
        if graph[i][j] == 1: # 벽일때 안 헷갈리게 -1로
            graph[i][j] = -1

virus_num = len(viruses)

def zero_count(graph, visited, N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and not visited[i][j]:
                cnt += 1
    
    return cnt
    
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

best = 2501
    
virus_combinations = combinations(range(virus_num), M)
for virus_combination in virus_combinations:
    temp_graph = [g[:] for g in graph]
    visited = [[False]*(N) for _ in range(N)]

    queue = deque([])
    for i in range(virus_num):
        if i in virus_combination:
            queue.append((viruses[i][0], viruses[i][1])) # 활성 상태
            visited[viruses[i][0]][viruses[i][1]] = True
            temp_graph[viruses[i][0]][viruses[i][1]] = 0
        else:
            temp_graph[viruses[i][0]][viruses[i][1]] = '*' # 비활성 상태

    clean = zero_count(temp_graph, visited, N) # 바이러스가 안퍼진 구역 개수

    if clean == 0: # 바이러스가 안퍼진 구역 개수가 아예 없음
        best = 0
        break
    
    time = 0
    while queue:
        x, y = queue.popleft()
        time = temp_graph[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            condition = (0 <= nx < N) and (0 <= ny < N) # 범위 내
            if condition and temp_graph[nx][ny] != -1 and not visited[nx][ny] and clean > 0: # 아직 방문 안하고, 벽이 아니고, 바이러스가 다 퍼진 상태가 아님
                if temp_graph[nx][ny] == 0:
                    clean -= 1 # 깨끗한 구역에서 새로 오염 됨
                temp_graph[nx][ny] = temp_graph[x][y] + 1 # 바이러스 전파
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if clean == 0: # 전부 오염된 경우
        best = min(best, time)


if best == 2501: # 변화 없음
    print(-1)
else:
    print(best)