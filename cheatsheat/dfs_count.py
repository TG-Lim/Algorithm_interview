# 백준 2667번 참고
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, visited, cnt):
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny, visited, cnt)
        return cnt
    return cnt

cnt = 0
for i in range(n):
    for j in range(n):
        search =  dfs(i, j, visited, cnt)
        if search != 0:
            print(search)

print(cnt)