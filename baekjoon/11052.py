N = int(input())
array = [0]
array.extend(list(map(int, input().strip().split())))

dp = [0]*(N+1)

for i in range(1, N+1):
    dp[i] = array[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j]+array[j])

print(dp[N])