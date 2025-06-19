from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            
            else:
                fuel += gas[i] - cost[i]
        
        return start
        


if __name__ == '__main__':
    cases = [
        [[1,2,3,4,5], [3,4,5,1,2]],
        [[2,3,4], [3,4,3]]
    ]

    for case in cases:
        output = Solution().canCompleteCircuit(case[0], case[1])
        print(output)