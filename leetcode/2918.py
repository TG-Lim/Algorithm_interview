from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, delta1 = sum(nums1), sum([n == 0 for n in nums1])
        sum2, delta2 = sum(nums2), sum([n == 0 for n in nums2])

        if sum1 + delta1 == sum2 + delta2:
            return sum1 + delta1
        
        if delta1 > 0 and delta2 > 0: # 더 큰 값 임의로 할당 가능해서 값 같게 가능
            return max(sum1+delta1, sum2+delta2)
        
        elif delta1 > 0 and delta2 == 0:
            if sum1 + delta1 <= sum2:
                return sum2
            else:
                return -1
        
        elif delta1 == 0 and delta2 > 0:
            if sum1 >= sum2 + delta2:
                return sum1
            else:
                return -1
            
        elif delta1 == 0 and delta2 == 0: # 합이 같은 경우는 앞에서 미리 나와서 그냥 -1 반환
            return -1

if __name__ == '__main__':
    cases = [
        [[3,2,0,1,0], [6,5,0]], # 12
        [[2,0,2,0], [1,4]], # -1
        [[8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11]], # 179
        [[2,5,6], [2, 4, 4]], # -1
    ]

    for case in cases:
        output = Solution().minSum(case[0], case[1])
        print(output)