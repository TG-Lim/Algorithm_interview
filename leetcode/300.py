class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

cases = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

if __name__ == '__main__':
    for case in cases:
        output = Solution().lengthOfLIS(case)
        print(output)