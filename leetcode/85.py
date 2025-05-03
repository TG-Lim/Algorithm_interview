class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        R, C = len(matrix), len(matrix[0])
        height = [0]*C
        left = [0]*C
        right = [C]*C
        max_area = 0

        for i in range(R):
            cur_left, cur_right = 0, C

            # 높이
            for j in range(C):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(C):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in reversed(range(C)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = C
                    cur_right = j
            
            for j in range(C):
                max_area = max(max_area, (right[j]-left[j])*height[j])
        
        return max_area

if __name__ == '__main__':
    cases = [
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], # 6
        [["0"]], # 0
        [["1"]], # 1
        [["1","0","1","0","0"],["1","1","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], # 10
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","0"],["1","0","0","1","0"]], # 4
        [["1","0","1","0","0"],["1","1","1","1","1"],["1","1","1","1","0"],["1","0","0","1","0"]], # 8
    ]

    for case in cases:
        output = Solution().maximalRectangle(case)
        print(output)