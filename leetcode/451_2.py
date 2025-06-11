from typing import List
from itertools import combinations
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        answer = [[None]*(n-k+1) for _ in range(m-k+1)]
        for r in range(m):
            for c in range(n):
                if r + k <= m and c + k <= n: # 범위 안
                    sub_array = set([grid[i][j] for i in range(r, r+k) for j in range(c, c+k)])
                    if len(sub_array) == 1:
                        answer[r][c] = 0
                        continue
                    else:
                        combs = combinations(sub_array, 2)
                        temp = float('inf')
                        for comb in combs:
                            temp = min(temp, abs(comb[0]-comb[1]))
                        answer[r][c] = temp
        
        return answer


if __name__ == '__main__':
    cases = [
        [[[1,8],[3,-2]], 2], # [[2]]
        [[[1,-2,3],[2,3,5]],2], # [[1, 2]]
        [[[3,-1]],1], # [[0, 0]]
    ]

    for case in cases:
        output = Solution().minAbsDiff(case[0], case[1])
        print(output)