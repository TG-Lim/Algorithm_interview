import sys
n = int(sys.stdin.readline().strip('\n'))
house = []
for _ in range(n):
    temp = map(int, sys.stdin.readline().strip('\n'))
    house.append(list(temp))

visited = [[False]*n for _ in range(n)]

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, 1, -1]

def dfs(row: int, col: int):
    if row < 0 or row >= n or col < 0 or col >= n or visited[row][col] or house[row][col] == 0:
        return 0

    visited[row][col] = True
    length = 1  # 현재 위치를 방문했으므로 길이는 1부터 시작

    # 상하좌우 이동
    for direction in range(4):
        next_row, next_col = row + delta_row[direction], col + delta_col[direction]
        length += dfs(next_row, next_col)  # 인접한 노드를 재귀적으로 방문하여 길이를 누적

    return length

# 각 연결된 부분의 길이를 저장할 리스트
lengths = []
for row in range(n):
    for col in range(n):
        if house[row][col] == 1 and not visited[row][col]:
            lengths.append(dfs(row, col))

# 결과 출력
print(len(lengths))
lengths.sort()
for l in lengths:
    print(l)