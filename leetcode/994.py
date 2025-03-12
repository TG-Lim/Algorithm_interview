from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def check_all_rotten(grid: list[list[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    cnt = 0
    rotten = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                cnt += 1
            if grid[i][j] == 2:
                rotten += 1

    if cnt > 0 and cnt == rotten:
        return True
    else:
        return False

def check_all_zero(grid: list[list[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                return False

    return True

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if check_all_zero(grid):
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        rottens = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottens.append((0, i, j))
                    visited[i][j] = True

        queue = deque(rottens)

        while queue:
            t, r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0<= nr < m and 0<= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((t+1, nr, nc))

        if check_all_rotten(grid):
            return t
        else:
            return -1
if __name__ == '__main__':
    cases = [
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
        [[0]],
        [[0, 0]]
    ]

    for case in cases:
        output = Solution().orangesRotting(case)
        print(output)