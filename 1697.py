# Silver 1
# 0 <= N <= 100,000 -> O(NlogN)
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
visited = [False]*(k*2+3)

position = n
cnt = 0
queue = deque([[position, cnt]])

if n <= k:
    while position != k:
        position, level = queue.popleft()
        adj_list = [position-1, position+1, 2*position]
        if k in adj_list:
            cnt = level + 1
            break
        else:
            level += 1
            for i in adj_list:
                if 0 <= i < 2*k+3 and not visited[i]:
                    queue.append([i, level])
                    visited[i] = True

    print(cnt)
else:
    print(n-k)