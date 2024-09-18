# Gold 5
# DP
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    numbers = []
    for _ in range(T):
        numbers.append(int(input()))

    maximum = max(numbers)

    dp = [0] * (maximum + 1)
    dp[0] = 1  # 합이 0인 경우는 한 가지 방법

    for num in [1, 2, 3]:
        for i in range(num, maximum + 1):
            dp[i] += dp[i - num]

    for number in numbers:
        print(dp[number])