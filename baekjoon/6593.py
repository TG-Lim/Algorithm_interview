from collections import deque
import sys

input = sys.stdin.readline

dl = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    def is_range(l, r, c):
        if 0 <= l < L and 0 <= r < R and 0 <= c < C:
            return True
        else:
            return False

    buildings = []
    start = end = None

    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().strip())
            floor.append(row)
            for c in range(C):
                if row[c] == 'S':
                    start = (0, l, r, c)
        buildings.append(floor)
        input()  # 층과 층 사이 빈 줄 제거용
    if L == 1 and R == 1 and C == 1:
        print("Escaped in 0 minute(s).")
        continue
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    queue = deque([start])
    visited[start[1]][start[2]][start[3]] = True
    is_escape = False
    escape_time = None

    while queue:
        t, l, r, c = queue.popleft()
        if buildings[l][r][c] == 'E':
            is_escape = True
            escape_time = t
        for i in range(6):
            nl, nr, nc = l + dl[i], r + dr[i], c + dc[i]
            if is_range(nl, nr, nc) and not visited[nl][nr][nc] and buildings[nl][nr][nc] != '#':
                visited[nl][nr][nc] = True
                queue.append((t+1, nl, nr, nc))

    if is_escape:
        print(f'Escaped in {escape_time} minute(s).')
    else:
        print('Trapped!')