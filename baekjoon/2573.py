# Gold 4
# BFS
import sys
from collections import deque
N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

def all_melt(array):
    cnt = 0
    for a in array:
        cnt += sum(a)
    if cnt == 0:
        return True
    else:
        return False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, visited):
    if array[i][j] != 0 and not visited[i][j]:
        queue = deque([])
        queue.append((i, j))
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                condition = (0 <= nx < N) and (0 <= ny < M)
                if condition and not visited[nx][ny] and array[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        return True
    else: # 이미 방문했거나 녹은 경우
        return False

def melt_iceberg(array):
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                condition = (0 <= ni < N) and (0 <= nj < M)
                if condition and array[ni][nj] == 0:
                    cnt += 1
            temp[i][j] = max(0, array[i][j]-cnt)
    return temp

answer = 0
while not all_melt(array):
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if bfs(i, j, visited):
                cnt += 1
    if cnt == 1: # 얼음이 한 덩어리
        answer += 1
        array = melt_iceberg(array)
    else: # 얼음이 여러 덩어리
        print(answer)
        exit()
print(0)