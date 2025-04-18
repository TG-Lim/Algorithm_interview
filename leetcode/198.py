class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums) # index 까지 훔쳤을 때 최대값
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) # i번째 안훔치는 경우와 훔치는 경우 비교
        
        return dp[-1]

cases = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
    [0],
    [2, 1],
    [2, 1, 1, 2]
]

if __name__ == '__main__':
    for case in cases:
        output = Solution().rob(case)
        print(output)