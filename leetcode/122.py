class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer, stock = 0, prices[0]

        for price in prices[1:]:
            if price > stock:
                answer += price - stock
            
            stock = price

        return answer

if __name__ == '__main__':
    cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1]
    ]

    for case in cases:
        output = Solution().maxProfit(case)
        print(output)