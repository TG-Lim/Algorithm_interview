# Silver 1
# 1<= n <= 10,000 -> O(N^2)
import sys

n = int(input())
array = [0]
for _ in range(n):
    array.append(int(sys.stdin.readline()))
    
if n <= 2: # 두 잔 보다 작은 경우
    print(sum(array))
    exit()
else: # 세 잔 이상
    dp = [0 for _ in range(n+1)]
    dp[1] = array[1]
    dp[2] = array[1] + array[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i], dp[i-1])

    print(dp[n])
    exit()