from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1, 1, 0, 0]
        dc = [0, 0, 1, -1]
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(r, c):
            if not visited[r][c]:
                visited[r][c] = True
                if grid[r][c] == '1':
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0<= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and not visited[nr][nc]:
                            dfs(nr, nc)
                    return True
                return False
            else:
                return False
        
        answer = 0
        for r in range(m):
            for c in range(n):
                if dfs(r, c):
                    answer += 1

        return answer


if __name__ == '__main__':
    cases = [
        [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
        [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    ]

    for case in cases:
        output = Solution().numIslands(case)
        print(output)