# Gold 3
# 5 <= N, M <= 100
import sys
sys.setrecursionlimit(int(1e9))
from collections import deque

N, M = map(int, input().strip().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

air = set()
def dfs(x, y):
    if (x, y) not in air:
        air.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and array[nx][ny] == 0:
                dfs(nx, ny)
    return
# 바깥 공기 초기화
dfs(0, 0)


queue = deque()
for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            queue.append((i, j, 0))

previous_t = 0
melt_cand = []
while queue:
    x, y, t = queue.popleft()
    if t != previous_t: # 이전이랑 시간 바뀜
        for cx, cy in melt_cand:
            array[cx][cy] = 0
            dfs(cx, cy)
        previous_t = t
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) in air: # 바깥 공기 인 경우만 카운트 추가
            cnt += 1
    if cnt >= 2: # 치즈 녹는 경우
        melt_cand.append((x, y))
    else: # 치즈 안녹음
        queue.append((x, y, t+1))

print(previous_t+1)