# Gold 4
# 구현, BFS
from collections import deque

R, C, T = map(int, input().strip().split())
array = []
for _ in range(R):
    array.append(list(map(int, input().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    if array[i][0] == -1:
        air1 = i
        air2 = i+1
        break

def bfs():
    queue = deque([])
    # 먼지를 확산 시킬 후보군들 큐에 삽입
    for i in range(R):
        for j in range(C):
            if array[i][j] > 0:
                queue.append((i, j, array[i][j])) # x, y, 먼지양
    
    while queue:
        x, y, dust = queue.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            condition = (0 <= nx < R) and (0 <= ny < C)
            if condition and array[nx][ny] != -1: # 범위 안 이고, 공기 청정기 미 설치 영역
                array[nx][ny] += (dust//5)
                cnt += 1
        array[x][y] -= cnt*(dust//5)
    
def wind():
    # 위쪽 공기 청정기
    for i in range(air1-1, 0, -1):  # 공기 청정기로 -> 아래부터 위로
        array[i][0] = array[i-1][0]
    
    for i in range(C-1):  # 동쪽으로
        array[0][i] = array[0][i+1]
    
    for i in range(air1):  # 남쪽으로
        array[i][C-1] = array[i+1][C-1]
    
    for i in range(C-1, 1, -1):  # 서쪽으로
        array[air1][i] = array[air1][i-1]
    array[air1][1] = 0
    
    # 아래쪽 공기 청정기
    for i in range(air2+1, R-1):  # 공기 청정기로 -> 아래부터 위로
        array[i][0] = array[i+1][0]
    
    for i in range(C-1):  # 동쪽으로
        array[R-1][i] = array[R-1][i+1]
    
    for i in range(R-1, air2, -1):  # 북쪽으로
        array[i][C-1] = array[i-1][C-1]
    
    for i in range(C-1, 1, -1):  # 서쪽으로
        array[air2][i] = array[air2][i-1]
    array[air2][1] = 0

for _ in range(T):
    bfs()
    wind()

total = 0
for a in array:
    total += sum(a)
print(total+2)