class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = int(1e6)

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
        

if __name__ == '__main__':
    cases = [
        [7,1,5,3,6,4],
        [7,6,4,3,1]
    ]

    for case in cases:
        solution = Solution()
        print(solution.maxProfit(prices=case))