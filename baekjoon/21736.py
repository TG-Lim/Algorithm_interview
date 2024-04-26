# Silver2
# 1<= N, M M= 600 -> O(N^3)
import sys
from collections import deque
N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(sys.stdin.readline().rstrip()))
visited = [[False]*M for _ in range(N)]

cnt = 0
start_x = 0
start_y = 0
for i in range(N):
    for j in range(M):
        if array[i][j] == 'I':
           start_x = i
           start_y = j

queue = deque([(start_x, start_y)])
visited[start_x][start_y] = True
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        condition = (0<= nx < N) and (0 <= ny < M)
        if condition and visited[nx][ny] == False and array[nx][ny] != "X":
            visited[nx][ny] = True
            if array[nx][ny] == "P":
                cnt += 1
            queue.append((nx, ny))

if cnt == 0:
    print("TT")
else:
    print(cnt)