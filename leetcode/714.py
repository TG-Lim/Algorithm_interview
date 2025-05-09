from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0 # 실현 이익
        hold = float('inf') # 싸게 산 가격
        for price in prices:
            cash = max(cash, price - hold - fee)
            hold = min(hold, price - cash)
        return cash


if __name__ == '__main__':
    cases = [
        [[1,3,2,8,4,9], 2],
        [[1,3,7,5,10,3], 3]
    ]

    for case in cases:
        output = Solution().maxProfit(case[0], case[1])
        print(output)