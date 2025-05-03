from collections import deque

def solution():
    R, C, K = map(int, input().strip().split())
    array = [list(input().strip()) for _ in range(R)]
    
    queue = deque([(R-1, 0, 1, [(R-1, 0)])]) # r, c, 현재 길이, 방문 관련 집합. 초기에는 제일 구석

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = 0

    while queue:
        r, c, t, visited = queue.popleft()
        if r == 0 and c == C-1 and t == K:
            answer += 1
            continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and t < K and array[nr][nc] == '.' and (nr, nc) not in visited:
                new_visited = visited[:]
                new_visited.append((nr, nc))
                queue.append((nr, nc, t+1, new_visited))

    print(answer)

solution()