class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        pass

if __name__ == '__main__':
    cases = [
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
        [["0"]],
        [["1"]]
    ]

    for case in cases:
        output = Solution().maximalRectangle(case)
        print(output)