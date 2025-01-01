class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        answer = 0
        for i in range(1, n+1):
            answer += nums[2*(i-1)]
        
        return answer


if "__main__" == __name__:
    cases = [
        [1, 4, 3, 2],
        [6, 2, 6, 5, 1, 2]
    ]

    for case in cases:
        solution = Solution()
        print(solution.arrayPairSum(nums=case))