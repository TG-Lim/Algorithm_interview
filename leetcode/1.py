class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in nums[i+1:]:
                return [i, nums[i+1:].index(i)+(i+1)]
            
            
if __name__ == "__main__":
    cases = [
        [
            [2, 7, 11, 15], 9
        ],
        [
            [3, 2, 4], 6
        ],
        [
            [3, 3]
        ]
    ]