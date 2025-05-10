from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = float('-inf')
        cash = 0

        for price in prices:
            prev_cash = cash
            prev_hold = hold
            hold = max(prev_hold, prev_cash - price)
            cash = max(prev_cash, price + prev_hold - fee)
        
        return cash
if __name__ == '__main__':
    cases = [
        [[1,3,2,8,4,9], 2], # 8
        [[1,3,7,5,10,3], 3], # 6
    ]

    for case in cases:
        output = Solution().maxProfit(case[0], case[1])
        print(output)