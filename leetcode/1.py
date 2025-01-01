class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]


cases = [
    [[2, 7, 11, 15], 9],
    [[3, 2, 4], 6],
    [[3, 3], 6]
]

if __name__ == '__main__':
    for case in cases:
        solution = Solution()
        nums, target = case[0], case[1]
        answer = solution.twoSum(nums=nums, target=target)

        print(answer)


"""
Function twoSum(nums, target):
    Initialize nums_map as an empty dictionary
    For i from 0 to len(nums) - 1:
        nums_map[nums[i]] = i

    For i from 0 to len(nums) - 1:
        complement = target - nums[i]
        If complement in nums_map and nums_map[complement] != i:
            Return [i, nums_map[complement]]
"""