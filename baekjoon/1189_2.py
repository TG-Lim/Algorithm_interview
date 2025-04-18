import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def solution():
    R, C, K = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    dr = (-1, 1, 0, 0)
    dc = (0, 0, 1, -1)
    answer = 0

    def dfs(r, c, depth):
        nonlocal answer

        # 남은 이동 횟수
        rem = K - depth

        # 남은 거리
        dist = r + abs(c-(C-1))

        if dist > rem: # 남은 거리가 횟수보다 큼
            return
        
        if depth == K:
            if r == 0 and c == C-1:
                answer += 1
            return
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] \
            and grid[nr][nc] == '.':
                visited[nr][nc] = True
                dfs(nr, nc, depth+1)
                visited[nr][nc] = False # 백트레킹 적용
    
    visited[R-1][0] = True
    dfs(R-1, 0, 1)

    print(answer)

solution()