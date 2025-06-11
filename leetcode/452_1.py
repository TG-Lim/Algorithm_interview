from typing import List
from itertools import combinations

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        length = len(nums)
        total_product = 1
        for n in nums:
            total_product *= n
        
        if int(total_product**0.5) != total_product**0.5: # 수 성립 못함
            return False

        for r in range(1, length):
            combs = combinations(range(length), r)
            for comb in combs:
                product = 1
                for c in comb:
                    product *= nums[c]
                if total_product / product == product and product == target:
                    return True
        return False

    
if __name__ == '__main__':
    cases = [
        [[3, 1, 6, 8, 4], 24],
        [[2, 5, 8, 7], 15],
        [[2, 8], 4],
        [[6,5,1,15,7,14], 686]
    ]

    for case in cases:
        output = Solution().checkEqualPartitions(case[0], case[1])
        print(output)