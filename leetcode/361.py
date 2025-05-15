from typing import List
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        up = [[0]*n for _ in range(m)]
        down = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        left = [[0]*n for _ in range(m)]

        # up
        for i in range(1, m):
            for j in range(n):
                if grid[i-1][j] == 'E':
                    up[i][j] = up[i-1][j] + 1
                elif grid[i-1][j] == 'W':
                    up[i][j] = 0 # 초기화
                else:
                    up[i][j] = up[i-1][j]
        
        # down
        for i in range(m-2, -1, -1):
            for j in range(n):
                if grid[i+1][j] == 'E':
                    down[i][j] = down[i+1][j] + 1
                elif grid[i+1][j] == 'W':
                    down[i][j] = 0
                else:
                    down[i][j] = down[i+1][j]

        # left
        for j in range(1, n):
            for i in range(m):
                if grid[i][j-1] == 'E':
                    left[i][j] = left[i][j-1] + 1
                elif grid[i][j-1] == 'W':
                    left[i][j] = 0
                else:
                    left[i][j] = left[i][j-1]

        ## right
        for j in range(n-2, -1, -1):
            for i in range(m):
                if grid[i][j+1] == 'E':
                    right[i][j] = right[i][j+1] + 1
                elif grid[i][j+1] == 'W':
                    right[i][j] = 0
                else:
                    right[i][j] = right[i][j+1]
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    answer = max(answer, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        return answer

if __name__ == '__main__':
    cases = [
        [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]],
        [["W","W","W"],["0","0","0"],["E","E","E"]]
    ]

    for case in cases:
        output = Solution().maxKilledEnemies(case)
        print(output)