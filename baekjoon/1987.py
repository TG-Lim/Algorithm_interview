# Gold 4
# BFS
from collections import deque

R, C = map(int, input().strip().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = []
for _ in range(R):
    array.append(list(input().strip()))

queue = deque()
# x, y, 경로, 길이
queue.append((0, 0, array[0][0], 1))

visited = {(0,0,array[0][0]): 1}

answer = 1

while queue:
    x, y, path, length = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if array[nx][ny] not in path: # 방문 안한 경우
                new_path = path + array[nx][ny]
                if (nx, ny, new_path) not in visited or visited[(nx, ny, new_path)] <= length:
                    visited[(nx, ny, new_path)] = length + 1 # 방문 안했거나 기존에 존재한 것 보다 짧은 경우 업데이트
                    queue.append((nx, ny, new_path, length+1))
                    answer = max(answer, length + 1)

print(answer)