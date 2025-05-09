from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = 50000

        for price in prices:
            hold = min(price, hold)
            profit = max(profit, price - hold)
        
        return profit

if __name__ == '__main__':
    cases = [
        [7,1,5,3,6,4],
        [7,6,4,3,1]
    ]

    for case in cases:
        output = Solution().maxProfit(case)
        print(output)