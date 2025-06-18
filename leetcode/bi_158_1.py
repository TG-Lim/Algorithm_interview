from typing import List
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        array = [(i, x[i], y[i]) for i in range(n)]
        array.sort(key=lambda x: -x[2])
        
        x_value = []
        y_value = []
        for i in range(n):
            if not y_value: # 없으면 넣기
                x_value.append(array[i][1])
                y_value.append(array[i][2])
            else:
                if array[i][1] not in x_value:
                    x_value.append(array[i][1])
                    y_value.append(array[i][2])
            
            if len(y_value) == 3:
                break
        
        if len(y_value) == 3:
            return sum(y_value)
        else:
            return -1


if __name__ == '__main__':
    cases = [
        [[1,2,1,3,2], [5,3,4,6,2]],
        [[1,2,1,2], [4,5,6,7]]
    ]

    for case in cases:
        output = Solution().maxSumDistinctTriplet(case[0], case[1])
        print(output)