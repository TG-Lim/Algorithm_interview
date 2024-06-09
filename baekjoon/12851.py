# Gold4
# BFS
from collections import deque

N, K = map(int, input().strip().split())

if N == K:
    print(0)
    print(1)
    exit()

visited = [200000 for _ in range(200001)]

answer_time = 200000
answer_cnt = 0
queue = deque([])

visited[N] = 0
queue.append((N, 0)) # 위치, 시간

while queue:
    pos, cnt = queue.popleft()
    if pos-1 == K and (cnt+1) <= answer_time: # -1
        answer_time = cnt+1
        answer_cnt += 1
    
    elif pos+1 == K and (cnt+1) <= answer_time: # +1
        answer_time = cnt+1
        answer_cnt += 1
    
    elif 2*pos == K and (cnt+1) <= answer_time: # 2*
        answer_time = cnt+1
        answer_cnt += 1
    
    else:
        if 0 <= pos - 1 <= 200000 and cnt+1 <= visited[pos-1]:
            visited[pos-1] = cnt+1
            queue.append((pos-1, cnt+1))
        
        if 0 <= pos + 1 <= 200000 and cnt+1 <= visited[pos+1]:
            visited[pos+1] = cnt+1
            queue.append((pos+1, cnt+1))

        if 0 <= 2*pos <= 200000 and cnt+1 <= visited[2*pos]:
            visited[2*pos] = cnt+1
            queue.append((2*pos, cnt+1))

print(answer_time)
print(answer_cnt)