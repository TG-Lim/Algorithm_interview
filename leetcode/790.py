class Solution:
    def numTilings(self, n: int) -> int:
        namerji = int(1e9) + 7
        dp = [0]*(1001)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[1]
        
        return dp[n]

if __name__ == '__main__':
    cases = [
        1, 2, 3, 4,5, 789
    ]

    for case in cases:
        output = Solution().numTilings(case)
        print(output)