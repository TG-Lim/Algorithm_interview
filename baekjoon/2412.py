import sys
from collections import deque

input = sys.stdin.readline
n, T = map(int, input().strip().split())

climbing = {t: [] for t in range(T+1)}
visited = {}
for _ in range(n):
    x, y = map(int, input().strip().split())
    visited[(x, y)] = False
    climbing[y].append((x, y))

queue = deque([(0, 0, 0)]) # x, y, t
while queue:
    x, y, t = queue.popleft()
    if y == T:
        print(t)
        exit()
    for h in range(y-2, y+3): # 높이 차이 0 - 2
        if 0 <= h <= T: # T까지만 있음
            for position in climbing[h]:
                if abs(position[0]-x) <= 2 and abs(position[1]-y) <= 2 and not visited[position]: # 조건 만족하고, 방문안함
                    visited[position] = True
                    queue.append((position[0], position[1], t+1))

print(-1)