from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = [0]*len(prices)
        sold = [0]*len(prices)
        rest = [0]*len(prices)

        hold[0] = -prices[0]
        sold[0] = 0
        rest[0] = 0

        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i]) # 샀았을 때 이득
            sold[i] = max(sold[i-1], prices[i]+hold[i-1]) # 팔았을 때 이득
            rest[i] = max(rest[i-1], sold[i-1]) # 쉬었을 때 이득. i-1 째 쉬는 거랑 i-1 때 판 거
        
        return max(sold[-1], rest[-1])