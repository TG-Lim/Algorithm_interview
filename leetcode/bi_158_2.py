from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # dp[i][t][h] = i번째 날, t번 거래 완료, holding 상태 h일 때 최대 수익
        # h = 0: 보유 없음, 1: 정상 주식 보유, 2: 공매도 보유
        dp = [[[-float('inf')] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
        
        # 초기 상태 설정: 0일차, 0번 거래, 보유 없음
        dp[0][0][0] = 0

        for i in range(n):  # day
            for t in range(k + 1):  # transaction count
                for h in range(3):  # holding status
                    if dp[i][t][h] == -float('inf'):
                        continue

                    # 1. 아무것도 안 함
                    dp[i + 1][t][h] = max(dp[i + 1][t][h], dp[i][t][h])

                    # 2. 행동 (holding 상태에 따라 다름)
                    if h == 0:
                        # 정상 매수 시도 → 보유 상태 1
                        dp[i + 1][t][1] = max(dp[i + 1][t][1], dp[i][t][0] - prices[i])
                        # 공매도 시작 → 보유 상태 2
                        dp[i + 1][t][2] = max(dp[i + 1][t][2], dp[i][t][0] + prices[i])

                    elif h == 1:
                        # 정상 매도 → 거래 완료되므로 t + 1
                        if t + 1 <= k:
                            dp[i + 1][t + 1][0] = max(dp[i + 1][t + 1][0], dp[i][t][1] + prices[i])

                    elif h == 2:
                        # 공매도 되사기 → 거래 완료되므로 t + 1
                        if t + 1 <= k:
                            dp[i + 1][t + 1][0] = max(dp[i + 1][t + 1][0], dp[i][t][2] - prices[i])

        # 최대 수익은 거래 t회 완료 후, 아무것도 보유하지 않은 상태에서의 수익 중 최댓값
        return max(dp[n][t][0] for t in range(k + 1))
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProfit([1,5,18,2,13,5,7,13], 4))  # ✅ 36
    print(sol.maximumProfit([1,13,11,6,2,11,18,14], 4))  # ✅ 33
    print(sol.maximumProfit([1,7,9,8,2], 2))  # ✅ 14
    print(sol.maximumProfit([12,16,19,19,8,1,19,13,9], 3))  # ✅ 36
