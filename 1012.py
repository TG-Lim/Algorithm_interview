# 50 X 50 => O(N^3) okay
# Silver 2
import sys
sys.setrecursionlimit(10000)

drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

def dfs(row, col, graph, visited):
    if row >= n or row < 0 or col >= m or col < 0:
        return False

    if visited[row][col] == False:
        visited[row][col] = True
        if graph[row][col] == 1:
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                dfs(nrow, ncol, graph, visited)
            return True
        else:
            return False

    return False

def calculate(m: int, n: int, k: int):
    graph = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().split())
        graph[j][i] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, graph, visited) == True:
                count += 1

    return count

T = int(sys.stdin.readline())
while T > 0:
    m, n, k = map(int, sys.stdin.readline().split())
    print(calculate(m, n, k))
    T -= 1