import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().strip().split())
array = [list(map(int, input().strip().split())) for _ in range(N)]

viruses = []
for r in range(N):
    for c in range(N):
        if array[r][c] == 2:
            viruses.append((r, c))

def calculate_time(temp_array: list[list[int]], comb: tuple):
    queue = deque([])

    for c in comb:
        queue.append((c[0], c[1], 0))

    while queue:
        r, c, t = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if temp_array[nr][nc] == 0: # 빈 칸
                    temp_array[nr][nc] = 2
                    queue.append((nr, nc, t+1))
    
    for r in range(N):
        for c in range(N):
            if temp_array[r][c] == 0: # 0이 존재. 덜 감염
                return -1
    
    return t

combs = combinations(viruses, M)

answer = int(1e6)

for comb in combs:
    temp_array = [a[:] for a in array]
    for v in viruses:
        if v not in comb:
            temp_array[v[0]][v[1]] = 0 # 안 퍼트릴 것들 0으로
    
    t = calculate_time(temp_array, comb)
    if t > -1:
        answer = min(answer, t)

if answer == int(1e6):
    print(-1)
else:
    print(answer)