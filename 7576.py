# 2 <= M, N <= 1000 -> 최대 O(N^2) complexity
# adjacency matrix 형태로 자료형 만들어도 될듯.
import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
field = []
tomato = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    field.append(data)
    for j in range(m):
        if field[i][j] == 1:
            tomato.append((0, i, j)) # row index, col index, day

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, 1, -1]
q = deque(tomato)
while q:
    day, row, col = q.popleft()
    for i in range(4):
        nrow = row + delta_row[i]
        ncol = col + delta_col[i]
        if 0 <= nrow < n and 0 <= ncol < m and field[nrow][ncol] == 0:
            field[nrow][ncol] = 1
            q.append((day+1, nrow, ncol))

for i in range(n):
    if 0 in field[i]:
        print(-1)
        sys.exit(0)
    
print(day)