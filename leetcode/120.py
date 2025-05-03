class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][0] = dp[i-1][0] + triangle[i][0]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] # 이전 인덱스와 현재 인덱스에서 값이 옴
        
        return min(dp[-1])
    

if __name__ == '__main__':
    cases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],
        [[-10]]
    ]

    for case in cases:
        output = Solution().minimumTotal(case)
        print(output)