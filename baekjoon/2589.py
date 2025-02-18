import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
islands = []
for _ in range(R):
    temp = list(input().strip())
    islands.append(temp)

lands = []
for r in range(R):
    for c in range(C):
        if islands[r][c] == 'L':
            lands.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def find_treasure_location(r, c):
    """
    find available treasure location
    """
    visited = [[False]*C for _ in range(R)]
    queue = deque([(0, r, c)])
    visited[r][c] = True
    while queue:
        t, nr, nc = queue.popleft()
        for i in range(4):
            nnr, nnc = nr + dr[i], nc + dc[i]
            if 0 <= nnr < R and 0 <= nnc < C and islands[nnr][nnc] == 'L' and not visited[nnr][nnc]: # 범위 내에 있고, 방문하지 않은 땅일 경우
                visited[nnr][nnc] = True
                queue.append((t+1, nnr, nnc))
                
    return t

answer = 0

for land in lands:
    score = find_treasure_location(land[0], land[1])
    answer = max(answer, score)
    
print(answer)