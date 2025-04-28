n = int(input())

if n == 0:
    print(0)
    print(0)
    exit()

dp = [0] * (abs(n)+2)
dp[0] = 0
dp[1] = 1

for i in range(2, abs(n)+1):
    dp[i] = (dp[i-1] + dp[i-2]) % int(1e9)

result = dp[abs(n)]

if n > 0:
    print(1)
    print(result)
else:
    if n % 2 == 0:  # n이 짝수면 부호가 음수
        print(-1)
    else:           # n이 홀수면 부호가 양수
        print(1)
    print(result)