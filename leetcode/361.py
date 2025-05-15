from typing import List
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        up = [[0]*n for _ in range(m)]
        down = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        left = [[0]*n for _ in range(m)]

        ## up
        for j in range(n):
            if grid[0][j] == 'E':
                up[0][j] = 1
            else:
                up[0][j] = 0
        
        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 'E':
                    up[i][j] = up[i-1][j] + 1
                
                elif grid[i][j] == 'W':
                    up[i][j] = 0 # 초기화
                
                else:
                    up[i][j] = up[i-1][j]
        
        ## down
        for j in range(n):
            if grid[-1][j] == 'E':
                down[-1][j] = 1
            else:
                down[-1][j] = 0
        
        for i in range(m-2, -1, -1):
            for j in range(n):
                if grid[i][j] == 'E':
                    down[i][j] = down[i+1][j] + 1
                elif grid[i][j] == 'W':
                    down[i][j] = 0
                else:
                    down[i][j] = down[i+1][j]

        ## left
        for i in range(m):
            if grid[i][0] == 'E':
                left[i][0] = 1
        
        for j in range(1, n):
            for i in range(m):
                if grid[i][j] == 'E':
                    pass      

if __name__ == '__main__':
    cases = [
        [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]],
        [["W","W","W"],["0","0","0"],["E","E","E"]]
    ]

    for case in cases:
        output = Solution().maxKilledEnemies(case)
        print(output)