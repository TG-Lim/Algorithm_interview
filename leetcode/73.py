from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        original_zero = set()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    original_zero.add((r, c))

        for r in range(R):
            for c in range(C):
                if (r, c) in original_zero:
                    for c2 in range(C):
                        matrix[r][c2] = 0
    
                    for r2 in range(R):
                        matrix[r2][c] = 0
                else:
                    continue
        

if __name__ == '__main__':
    print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))