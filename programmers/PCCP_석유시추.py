lands = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[-1]*m for _ in range(n)]
    space = {-1: 0}

    def bfs(x, y, l):
        nonlocal land, visited
        q = deque([(x, y)])
        visited[x][y] = l

        cnt = 1
        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = l
                    cnt += 1
        
        return cnt
    
    index = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1 and land[i][j] == 1:
                space[index] = bfs(i, j, index)
                index += 1
        

    answer = 0

    for i in list(zip(*visited)):
        temp = 0
        for j in set(i):
            temp += space[j]
        
        answer = max(answer, temp)
    
    return answer

for land in lands:
    print(solution(land))