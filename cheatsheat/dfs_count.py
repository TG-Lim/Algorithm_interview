# 백준 2667번 참고
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
