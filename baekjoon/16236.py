# Gold 3
# 그 유명한 아기상어 / DFS,BFS
from collections import deque
inf = int(1e9)

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

shark = 2
start_x, start_y = 0, 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            start_x, start_y = i, j
            array[start_x][start_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(): # BFS를 이용하여 최단거리로 이동할 수 있는 거리 테이블 제공 ***
    dist = [[-1]*N for _ in range(N)]
    queue = deque([(start_x, start_y)])
    dist[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            condition = (0 <= nx < N) and (0 <= ny < N)
            if condition and dist[nx][ny] == -1 and array[nx][ny] <= shark:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = inf
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 0 < array[i][j] < shark:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == inf:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        start_x, start_y = value[0], value[1]
        result += value[2]
        array[start_x][start_y] = 0
        ate += 1
        if ate >= shark:
            shark += 1
            ate = 0