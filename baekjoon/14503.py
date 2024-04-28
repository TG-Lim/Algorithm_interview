# Gold 5
# 3 <= N, M <= 50
from collections import deque
N, M = map(int, input().split())
start_x, start_y, direction = map(int, input().split())

def change_direction(direction: int):
    if direction == 0:
        return 3
    else:
        return direction-1

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

queue = deque([])
queue.append((start_x, start_y))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1] # 북 동 남 서
cnt = 0

while queue:
    x, y = queue.popleft()
    if array[x][y] == 0:
        array[x][y] = 2
        cnt += 1
    clean = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        condition = (0<= nx < N) and (0 <= ny < M)
        if condition and array[nx][ny] == 0: # 청소 못한 칸 있을 경우
            clean = False
    if clean:
        nx = x - dx[direction] # 후진
        ny = y - dy[direction] # 후진
        condition = (0 <= nx < N) and (0 <= ny < M)
        if condition and array[nx][ny] != 1: # 0 또는 2
            queue.append((nx, ny))
        # queue에는 항상 하나의 원소만 있으므로 이 조건 성립 못하면 정지됨
    else: # 더러운 경우
        direction = change_direction(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        if array[nx][ny] == 0: # 청소 X 인 경우 전진
            queue.append((nx, ny))
        else: # 전진 못한 경우 큐에 다시 넣어줘야 함
            queue.append((x, y))

print(cnt)