from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum > 0:
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]: # 중복 제거용
                        left += 1
                    while left < right and nums[right] == nums[right-1]: # 중복 제거용
                        right -= 1
                    
                    left += 1
                    right -= 1 # 찾았으니 다음걸로
            
        return result