from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        
        for i in range(N):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        return max(dp)

if __name__ == '__main__':
    cases = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8]
    ]

    for case in cases:
        output = Solution().maxSubArray(case)
        print(output)