from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        for i in range(len(arr)-2):
            temp = arr[i:i+3]
            if all(t % 2 == 1 for t in temp):
                return True
        
        return False
        
if __name__ == '__main__':
    cases = [
        [2,6,4,1],
        [1,2,34,3,4,5,7,23,12],
        [1, 1, 1],
        [1, 4, 1, 1]
    ]

    for case in cases:
        output = Solution().threeConsecutiveOdds(case)
        print(output)