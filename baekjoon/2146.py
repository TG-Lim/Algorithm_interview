# Gold 3
import sys
from collections import deque
from itertools import combinations


input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

boundaries = []
visited = [[False]*N for _ in range(N)]

def bfs(i, j, boundary):
    visited[i][j] = True # 방문 처리
    queue = deque([(i, j)])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N: # 영역 내
                if array[nr][nc] == 0: # 인접한 구역이 바다
                    boundary.add((r, c))
                elif array[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    return boundary

for i in range(N):
    for j in range(N):
        if not visited[i][j] and array[i][j] == 1:
            island_boundary = bfs(i, j, set([]))
            boundaries.append(island_boundary)

answer = 201

combination = combinations(boundaries, 2)
for comb in combination:
    island1, island2 = comb[0], comb[1]
    for l1 in island1:
        for l2 in island2:
            distance = abs(l1[0]-l2[0])+abs(l1[1]-l2[1])-1
            answer = min(answer, distance)

print(answer)