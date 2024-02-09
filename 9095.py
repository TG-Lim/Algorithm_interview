# Silver 3
import sys
n = int(sys.stdin.readline())

numbers = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    numbers.append(temp)

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for number in numbers:
    print(dp[number])