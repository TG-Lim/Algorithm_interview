# Gold 4
from collections import deque

N, K = map(int, input().split())
visited = [False]*(100001)

answer = int(1e9)

if N == K:
    print(0)
    exit()
    
queue = deque([])
queue.append((N, 0)) # 위치, 이동시간
visited[N] = True

while queue:
    x, n = queue.popleft()
    if x-1 == K or x+1 == K:
        answer = min(answer, n+1)
    if 2*x == K:
        answer = min(answer, n)
    
    else:
        if 0 <= 2*x <= 100000 and not visited[2*x]:
            visited[2*x] = True
            queue.append((2*x, n))
        if 0<= x-1 <= 100000 and not visited[x-1]:
            visited[x-1] = True
            queue.append((x-1, n+1))
        if 0 <= x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = True
            queue.append((x+1, n+1))


print(answer)