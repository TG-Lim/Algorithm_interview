# 2<= N, M <= 100 -> O(N^3) Time complexity
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# n : row index m : column index

miro = []
for _ in range(n):
    temp = map(int, sys.stdin.readline().strip('\n'))
    miro.append(list(temp))
    
delta_row = [1, -1, 0, 0]
delta_col = [0, 0, 1, -1]

q = deque([])
q.append((1, 0, 0))
while q:
    distance, row, col = q.popleft()
    for i in range(4):
        nrow = row + delta_row[i]
        ncol = col + delta_col[i]
        
        if 0<= nrow < n and 0 <= ncol < m and miro[nrow][ncol] == 1:
            miro[nrow][ncol] = distance + 1
            q.append((distance+1, nrow, ncol))

print(miro[n-1][m-1])