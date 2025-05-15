from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        
        nums.append(-float('inf'))
        peak_index = None

        for i in range(n):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peak_index = i
                break
                
        return peak_index


if __name__ == '__main__':
    cases = [
        [1, 2, 3, 1],
        [1,2,1,3,5,6,4],
        [1, 2],
        [1, 3, 4]
    ]

    for case in cases:
        output = Solution().findPeakElement(case)
        print(output)